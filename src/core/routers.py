from src.api.routers.user_routes import router as user_router
from src.api.routers.auth_google_routes import router as auth_google_router
from src.api.routers.direccion_routes import router as direccion_router
from src.api.routers.seccion_routes import router as seccion_router
from src.api.routers.categoria_routes import router as categoria_router
from src.api.routers.producto_routes import router as producto_router
from src.api.routers.color_routes import router as color_router
from src.api.routers.producto_color_routes import router as producto_color_router
from src.api.routers.talla_routes import router as talla_router
from src.api.routers.producto_talla_routes import router as producto_talla_router
from src.api.routers.carrito_routes import router as carrito_router
from src.api.routers.carrito_item_routes import router as carrito_item_router
from src.api.routers.imagen_routes import router as imagen_router
from src.api.routers.pedido_routes import router as pedido_router
from src.api.routers.pedido_item_routes import router as pedido_item_router
from src.api.routers.factura_routes import router as factura_router
from src.api.routers.promocion_routes import router as promocion_router


# nuevas rutas
from src.modules.auth.presentation.routes import router as auth_routes
from src.modules.usuarios.presentation.routes import router as usuario_routes