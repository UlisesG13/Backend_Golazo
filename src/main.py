import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import settings
from src.core.routers import api_router

app = FastAPI(
    title="Golazo",
    description="Backend del e-commerce Golazo",
    version="1.1.0"
)

# Middleware (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/", tags=["Root"])
def root():
    return {"message": "Bienvenido a Golazo API"}

if __name__ == "__main__":
    print("Docs disponible en: http://127.0.0.1:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
