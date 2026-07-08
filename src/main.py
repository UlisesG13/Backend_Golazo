import time
import uuid
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from src.core.config import settings
from src.core.limiter import limiter
from src.core.routers import api_router
from src.core.logging import setup_logging, get_logger
from src.core.database import engine
from src.shared.infra.messaging.fcm_client import init_firebase

setup_logging()
logger = get_logger("main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando aplicación...")
    init_firebase()
    yield
    logger.info("Apagando aplicación...")
    await engine.dispose()


app = FastAPI(
    title="Golazo-API",
    description="API del e-commerce Golazo, en constante actualizacion y mejoria",
    docs_url="/docs",
    redoc_url="/redoc",
    version="2.0.4",
    lifespan=lifespan,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Excepción no controlada: %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=500,
        content={"detail": "Error interno del servidor"},
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = uuid.uuid4().hex[:8]
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    logger.info(
        "%s %s %s %s %.0fms",
        request_id, request.method, request.url.path,
        response.status_code, duration,
    )
    return response


app.include_router(api_router, prefix="/api")


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Bienvenido a Golazo API"}


if __name__ == "__main__":
    print("Documentacion Interactiva: http://127.0.0.1:8000/docs")
    print("Documentacion Descriptiva: http://127.0.0.1:8000/redoc")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
