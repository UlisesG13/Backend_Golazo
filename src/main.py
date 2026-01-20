from src.core.config import app
from src.core.routers import (
    user_router, 
    auth_google_router, 
    direccion_router, 
    seccion_router, 
    categoria_router,
    producto_router,
    color_router,
    producto_color_router,
    talla_router,
    producto_talla_router
)

app.include_router(user_router)
app.include_router(auth_google_router)
app.include_router(direccion_router)
app.include_router(seccion_router)
app.include_router(categoria_router)
app.include_router(producto_router)
app.include_router(color_router)
app.include_router(producto_color_router)
app.include_router(talla_router)
app.include_router(producto_talla_router)

print("Docs: http://127.0.0.1:8000/docs")
@app.get("/")
def root():
    return {"message": "Bienvenido a Golazo"}