from fastapi import APIRouter

from src.api.routers.factura_routes import router as factura_router
# nuevas rutas
from src.modules.auth.presentation.routes import router as auth_routes
from src.modules.carrito.presentation.carrito_routes import router as carrito_router
from src.modules.catalogo.presentation.category.categoria_routes import router as categoria_router
from src.modules.catalogo.presentation.colors.color_routes import router as color_router
from src.modules.catalogo.presentation.images.image_routes import router as images_routes
from src.modules.catalogo.presentation.products.products_routes import router as products_routes
from src.modules.catalogo.presentation.section.seccion_routes import router as seccion_router
from src.modules.catalogo.presentation.sizes.talla_routes import router as talla_router
from src.modules.usuarios.presentation.direccion_routes import router as direccion_routes
from src.modules.usuarios.presentation.user_routes import router as usuario_routes
from src.modules.ventas.presentation.pedido.pedido_routes import router as pedido_router
from src.modules.ventas.presentation.promocion.promocion_routes import router as promocion_router

api_router = APIRouter()

# Ruta de las facturas
api_router.include_router(factura_router, prefix="/facturas", tags=["facturas"])

"""
----------------------------------------
|        RUTAS REFACTORIZADAS          |
----------------------------------------
"""
# Ruta de autenticacion (Login, Register, etc)
api_router.include_router(auth_routes, prefix="/auth", tags=["auth"])
# Ruta de las direcciones de los usuarios
api_router.include_router(direccion_routes, prefix="/users/direcciones", tags=["direcciones"])
# Ruta de los usuarios
api_router.include_router(usuario_routes, prefix="/users", tags=["users"])
# Ruta de los productos del catalogo
api_router.include_router(products_routes, prefix="/productos", tags=["catalogo"])
# Ruta de las imagenes de los productos
api_router.include_router(images_routes, prefix="/imagenes", tags=["imagenes"])

# Rutas de las secciones de los productos
api_router.include_router(seccion_router, prefix="/secciones", tags=["secciones"])

# Rutas de las categorias de los productos
api_router.include_router(categoria_router, prefix="/categorias", tags=["categorias"])

# Ruta de las tallas de un producto
api_router.include_router(talla_router, prefix="/tallas", tags=["tallas"])

# Ruta de los colores de un producto
api_router.include_router(color_router, prefix="/colores", tags=["colores"])

# Ruta del carrito
api_router.include_router(carrito_router, prefix="/carritos", tags=["carritos"])

# Ruta de las promociones
api_router.include_router(promocion_router, prefix="/promociones", tags=["promociones"])

# Ruta de los pedidos
api_router.include_router(pedido_router, prefix="/pedidos", tags=["pedidos"])
