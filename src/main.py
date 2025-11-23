from fastapi import FastAPI
from src.api.routers.user_routes import router as user_router
app = FastAPI(
    title="Golazo",
    description="Backend del e-commerce Golazo",
    version="0.0.2"
)
app.include_router(user_router)
@app.get("/")
def root():
    return {"message": "Bienvenido a Golazo"}
