from src.core.config import app
from src.core.routers import (
    seccion_router,
    categoria_router,
    producto_router,
    color_router,
    producto_color_router,
    talla_router,
    producto_talla_router,
    carrito_router,
    carrito_item_router,
    imagen_router,
    pedido_router,
    pedido_item_router,
    factura_router,
    promocion_router,
    auth_routes,
    usuario_routes,
    direccion_routes
)

app.include_router(seccion_router)
app.include_router(categoria_router)
app.include_router(producto_router)
app.include_router(color_router)
app.include_router(producto_color_router)
app.include_router(talla_router)
app.include_router(producto_talla_router)
app.include_router(carrito_router)
app.include_router(carrito_item_router)
app.include_router(imagen_router)
app.include_router(pedido_router)
app.include_router(pedido_item_router)
app.include_router(factura_router)
app.include_router(promocion_router)

# nuevas rutas

app.include_router(auth_routes)
app.include_router(usuario_routes)
app.include_router(direccion_routes)

print("Docs: http://127.0.0.1:8000/docs")
@app.get("/")
def root():
    return {"message": "Bienvenido a Golazo"}