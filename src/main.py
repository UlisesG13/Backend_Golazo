from src.core.config import app
from src.core.routers import user_router, auth_google_router

app.include_router(user_router)
app.include_router(auth_google_router)

@app.get("/")
def root():
    return {"message": "Bienvenido a Golazo"}