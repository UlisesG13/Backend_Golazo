from src.api.routers.seccion_routes import router as seccion_router
from src.api.routers.categoria_routes import router as categoria_router
from src.api.routers.color_routes import router as color_router
from src.api.routers.producto_color_routes import router as producto_color_router
from src.api.routers.talla_routes import router as talla_router
from src.api.routers.producto_talla_routes import router as producto_talla_router
from src.api.routers.carrito_routes import router as carrito_router
from src.api.routers.carrito_item_routes import router as carrito_item_router
from src.api.routers.pedido_routes import router as pedido_router
from src.api.routers.pedido_item_routes import router as pedido_item_router
from src.api.routers.factura_routes import router as factura_router
from src.api.routers.promocion_routes import router as promocion_router


# nuevas rutas
from src.modules.auth.presentation.routes import router as auth_routes
from src.modules.usuarios.presentation.user_routes import router as usuario_routes
from src.modules.usuarios.presentation.direccion_routes import router as direccion_routes
from src.modules.catalogo.presentation.products.products_routes import router as products_routes
from src.modules.catalogo.presentation.images.image_routes import router as images_routes