
# Backend – Arquitectura y estructura de Golazo

Backend en Python usando **FastAPI + SQLAlchemy**, organizado por capas siguiendo principios de **Clean Architecture / Hexagonal**.  
El objetivo es separar claramente responsabilidades, proteger el dominio y desacoplar infraestructura.

---

## Árbol Completo


```
├── core
│   ├── messaging
│   │   ├── di.py
│   │   ├── fcm_client.py
│   │   └── fcm_service.py
│   ├── config.py
│   ├── database.py
│   ├── exceptions.py
│   ├── logging.py
│   ├── routers.py
│   ├── security.py
│   └── supabase_config.py
├── modules
│   ├── auth
│   │   ├── application
│   │   │   ├── __init__.py
│   │   │   ├── generate_code.py
│   │   │   ├── get_by_google_id.py
│   │   │   ├── get_google_url.py
│   │   │   ├── login_user.py
│   │   │   ├── login_with_google.py
│   │   │   ├── register_user.py
│   │   │   ├── reset_password.py
│   │   │   ├── send_recovery_code.py
│   │   │   ├── verify_code.py
│   │   │   ├── verify_token.py
│   │   │   └── verify_user.py
│   │   ├── domain
│   │   │   ├── models.py
│   │   │   └── ports.py
│   │   ├── infra
│   │   │   ├── db
│   │   │   │   ├── repositories
│   │   │   │   │   ├── auth_repository.py
│   │   │   │   │   └── recovery_repository.py
│   │   │   │   └── tables
│   │   │   │       └── recovery_code.py
│   │   │   ├── google
│   │   │   │   └── google_oauth_service.py
│   │   │   ├── jwt
│   │   │   │   └── token_service.py
│   │   │   ├── messaging
│   │   │   │   └── email_service.py
│   │   │   └── security
│   │   │       └── password_service.py
│   │   └── presentation
│   │       ├── dependencies.py
│   │       ├── routes.py
│   │       └── schemas.py
│   ├── carrito
│   │   ├── app
│   │   │   ├── __init__.py
│   │   │   ├── add_item.py
│   │   │   ├── delete_carrito.py
│   │   │   ├── delete_item.py
│   │   │   ├── get_carrito.py
│   │   │   └── update_quantity.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── carrito_model.py
│   │   │   └── carrito_port.py
│   │   ├── infra
│   │   │   ├── carrito_repository.py
│   │   │   └── carrito_table.py
│   │   └── presentation
│   │       ├── carrito_dependencies.py
│   │       ├── carrito_dto.py
│   │       └── carrito_routes.py
│   ├── catalogo
│   │   ├── app
│   │   │   ├── categories
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create_category.py
│   │   │   │   ├── delete_category.py
│   │   │   │   ├── get_all_by_section.py
│   │   │   │   ├── get_all_categories.py
│   │   │   │   ├── get_category_by_id.py
│   │   │   │   └── update_category.py
│   │   │   ├── colors
│   │   │   │   ├── __init__.py
│   │   │   │   ├── asociar_color.py
│   │   │   │   ├── create_color.py
│   │   │   │   ├── delete_color.py
│   │   │   │   ├── desasociar_color.py
│   │   │   │   ├── get_all_color.py
│   │   │   │   ├── get_color_by_id.py
│   │   │   │   ├── get_color_by_producto.py
│   │   │   │   ├── get_p_color_by_id.py
│   │   │   │   └── update_color.py
│   │   │   ├── images
│   │   │   │   ├── __init__.py
│   │   │   │   ├── asociar_image_to_product.py
│   │   │   │   ├── delete_image.py
│   │   │   │   ├── delete_images_by_product.py
│   │   │   │   ├── desasociar_image_from_product.py
│   │   │   │   ├── get_images.py
│   │   │   │   ├── get_images_by_product.py
│   │   │   │   └── upload_imagen.py
│   │   │   ├── products
│   │   │   │   ├── __init__.py
│   │   │   │   ├── change_destacado.py
│   │   │   │   ├── change_status.py
│   │   │   │   ├── create_producto.py
│   │   │   │   ├── delete_producto.py
│   │   │   │   ├── get_producto_by_categoria.py
│   │   │   │   ├── get_producto_by_id.py
│   │   │   │   ├── list_products.py
│   │   │   │   └── update_producto.py
│   │   │   ├── sections
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create_seccion.py
│   │   │   │   ├── delete_seccion.py
│   │   │   │   ├── get_by_id_seccion.py
│   │   │   │   ├── get_secciones.py
│   │   │   │   └── update_seccion.py
│   │   │   └── sizes
│   │   │       ├── __init__.py
│   │   │       ├── asociar_talla.py
│   │   │       ├── create_talla.py
│   │   │       ├── delete_talla.py
│   │   │       ├── desasociar_talla.py
│   │   │       ├── get_all_tallas.py
│   │   │       ├── get_p_talla_by_id.py
│   │   │       ├── get_talla_by_id.py
│   │   │       ├── get_talla_by_producto.py
│   │   │       └── update_talla.py
│   │   ├── domain
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   ├── categoria_model.py
│   │   │   │   ├── color_model.py
│   │   │   │   ├── imagen_model.py
│   │   │   │   ├── producto_model.py
│   │   │   │   ├── seccion_model.py
│   │   │   │   └── talla_model.py
│   │   │   └── ports
│   │   │       ├── __init__.py
│   │   │       ├── categoria_port.py
│   │   │       ├── color_port.py
│   │   │       ├── imagen_port.py
│   │   │       ├── producto_port.py
│   │   │       ├── seccion_port.py
│   │   │       └── talla_port.py
│   │   ├── infra
│   │   │   ├── category
│   │   │   │   ├── category_repository.py
│   │   │   │   └── category_table.py
│   │   │   ├── colors
│   │   │   │   ├── color_repository.py
│   │   │   │   └── color_table.py
│   │   │   ├── images
│   │   │   │   ├── db
│   │   │   │   │   ├── image_repository.py
│   │   │   │   │   ├── image_table.py
│   │   │   │   │   └── product_image_repository.py
│   │   │   │   └── storage
│   │   │   │       └── supabase_storage_repository.py
│   │   │   ├── products
│   │   │   │   ├── product_repository.py
│   │   │   │   └── product_table.py
│   │   │   ├── sections
│   │   │   │   ├── seccion_repository.py
│   │   │   │   └── seccion_table.py
│   │   │   └── sizes
│   │   │       ├── talla_repository.py
│   │   │       └── talla_table.py
│   │   └── presentation
│   │       ├── category
│   │       │   ├── categoria_dependencies.py
│   │       │   ├── categoria_dto.py
│   │       │   └── categoria_routes.py
│   │       ├── colors
│   │       │   ├── color_dependencies.py
│   │       │   ├── color_dto.py
│   │       │   └── color_routes.py
│   │       ├── images
│   │       │   ├── image_dependencies.py
│   │       │   ├── image_routes.py
│   │       │   └── images_dto.py
│   │       ├── products
│   │       │   ├── product_dependencies.py
│   │       │   ├── product_dto.py
│   │       │   └── products_routes.py
│   │       ├── section
│   │       │   ├── seccion_dependencies.py
│   │       │   ├── seccion_dto.py
│   │       │   └── seccion_routes.py
│   │       └── sizes
│   │           ├── talla_dependencies.py
│   │           ├── talla_dto.py
│   │           └── talla_routes.py
│   ├── usuarios
│   │   ├── application
│   │   │   ├── direccion
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create_direccion.py
│   │   │   │   ├── delete_direccion.py
│   │   │   │   ├── get_all_direcciones.py
│   │   │   │   ├── get_direccion_by_id.py
│   │   │   │   ├── set_primary.py
│   │   │   │   └── update_direccion.py
│   │   │   ├── usuario
│   │   │   │   ├── __init__.py
│   │   │   │   ├── anonymize_user.py
│   │   │   │   ├── create_admin.py
│   │   │   │   ├── delete_user.py
│   │   │   │   ├── get_admins.py
│   │   │   │   ├── get_all_users.py
│   │   │   │   ├── get_user_by_email.py
│   │   │   │   ├── get_user_by_id.py
│   │   │   │   ├── register_device_token.py
│   │   │   │   └── update_user.py
│   │   │   └── __init__.py
│   │   ├── domain
│   │   │   ├── models.py
│   │   │   └── ports.py
│   │   ├── infra
│   │   │   ├── direccion_repository.py
│   │   │   ├── fcm_repository.py
│   │   │   ├── tables.py
│   │   │   └── user_repository.py
│   │   └── presentation
│   │       ├── direccion_dependencies.py
│   │       ├── direccion_routes.py
│   │       ├── schemas.py
│   │       ├── user_dependencies.py
│   │       └── user_routes.py
│   └── ventas
│       ├── app
│       │   ├── factura
│       │   │   ├── __init__.py
│       │   │   ├── change_status.py
│       │   │   ├── create_factura.py
│       │   │   ├── delete_factura.py
│       │   │   ├── get_all.py
│       │   │   ├── get_by_folio.py
│       │   │   ├── get_by_id.py
│       │   │   └── get_by_usuario.py
│       │   ├── pedido
│       │   │   ├── __init__.py
│       │   │   ├── change_status.py
│       │   │   ├── create_pedido.py
│       │   │   ├── get_by_id.py
│       │   │   ├── get_by_user.py
│       │   │   └── get_pedidos.py
│       │   └── promocion
│       │       ├── __init__.py
│       │       ├── change_status.py
│       │       ├── create_promocion.py
│       │       ├── delete_promocion.py
│       │       ├── get_all.py
│       │       ├── get_by_id.py
│       │       └── update_promocion.py
│       ├── domain
│       │   ├── __init__.py
│       │   ├── models.py
│       │   └── ports.py
│       ├── infra
│       │   ├── factura
│       │   │   ├── factura_repository.py
│       │   │   └── factura_table.py
│       │   ├── fcm
│       │   │   └── notificacion_repository.py
│       │   ├── pedido
│       │   │   ├── pedido_repository.py
│       │   │   └── pedido_table.py
│       │   └── promocion
│       │       ├── promocion_repository.py
│       │       └── promocion_table.py
│       └── presentation
│           ├── factura
│           │   ├── factura_di.py
│           │   ├── factura_dto.py
│           │   └── factura_routes.py
│           ├── pedido
│           │   ├── pedido_dependencies.py
│           │   ├── pedido_dto.py
│           │   └── pedido_routes.py
│           └── promocion
│               ├── promocion_dependencies.py
│               ├── promocion_dto.py
│               └── promocion_routes.py
├── shared
│   └── security.py
└── main.py
```

---

## Descripción por capa

### `api/`
Responsable únicamente de HTTP.
- Traduce requests → DTOs
- Llama a usecases
- Devuelve responses
No contiene lógica de negocio.

### `usecases/`
Capa de aplicación.
- Implementa reglas de negocio a nivel de casos de uso
## Árbol principal (resumido y anotado)

> **Tip:** Cada módulo sigue la misma estructura de capas (application, domain, infra, presentation) para mantener la coherencia y facilitar el mantenimiento.

```
├── core                # Utilidades y configuración global (no lógica de negocio)
│   ├── messaging       # Integración con servicios de mensajería (ej. FCM)
│   ├── config.py       # Carga y validación de variables de entorno
│   ├── database.py     # Inicialización de la base de datos y sesión
│   ├── exceptions.py   # Manejo centralizado de errores
│   ├── logging.py      # Configuración de logs
│   ├── routers.py      # Registro de rutas principales
│   ├── security.py     # Seguridad y utilidades criptográficas
│   └── supabase_config.py # Configuración de Supabase (almacenamiento)
├── modules             # Módulos funcionales, cada uno aislado
│   ├── auth            # Autenticación y autorización
│   │   ├── application # Casos de uso (login, registro, etc.)
│   │   ├── domain      # Modelos y contratos del dominio auth
│   │   ├── infra       # Implementaciones técnicas (DB, JWT, Google, etc.)
│   │   └── presentation# Rutas y dependencias FastAPI
│   ├── carrito         # Lógica de carrito de compras
│   │   ├── app         # Casos de uso del carrito
│   │   ├── domain      # Modelos y puertos del carrito
│   │   ├── infra       # Persistencia y acceso a datos
│   │   └── presentation# Rutas y DTOs del carrito
│   ├── catalogo        # Catálogo de productos, categorías, tallas, etc.
│   │   ├── app         # Casos de uso de catálogo
│   │   ├── domain      # Modelos y puertos del catálogo
│   │   ├── infra       # Persistencia y acceso a datos
│   │   └── presentation# Rutas y DTOs del catálogo
│   ├── usuarios        # Gestión de usuarios y direcciones
│   │   ├── application # Casos de uso de usuario
│   │   ├── domain      # Modelos y puertos de usuario
│   │   ├── infra       # Persistencia y acceso a datos
│   │   └── presentation# Rutas y DTOs de usuario
│   └── ventas          # Facturación, pedidos y promociones
│       ├── app         # Casos de uso de ventas
│       ├── domain      # Modelos y puertos de ventas
│       ├── infra       # Persistencia y acceso a datos
│       └── presentation# Rutas y DTOs de ventas
├── shared              # Utilidades compartidas entre módulos
│   └── security.py     # Funciones de seguridad reutilizables
└── main.py             # Punto de entrada de la aplicación FastAPI
```

> **Nota:** Cada subcarpeta dentro de `modules` representa un contexto de negocio independiente, siguiendo el principio de "bounded context".
```

### Capas y responsabilidades

#### `presentation/` (API)
Responsable únicamente de HTTP:
- Traduce requests → DTOs (Pydantic)
- Llama a casos de uso (application)
- Devuelve responses
> **Nunca contiene lógica de negocio.**

#### `application/` (Usecases)
Capa de aplicación:
- Implementa reglas de negocio a nivel de casos de uso
- Orquesta entidades del dominio y puertos
- No conoce FastAPI ni SQLAlchemy
> **Tip:** Aquí se valida la lógica de negocio y se aplican políticas.

#### `domain/`
Capa más importante:
- Modela el negocio (entidades, value objects)
- Define contratos (puertos/interfaces)
- No depende de ninguna otra capa
> **El dominio es intocable y estable.**

#### `infra/`
Detalles técnicos:
- Base de datos, ORM, servicios externos
- Implementa los contratos definidos en `domain/ports`
> **Nunca poner lógica de negocio aquí.**

#### `core/`
Soporte transversal:
- Configuración, logging, seguridad, inyección de dependencias
> **No contiene lógica de negocio, solo utilidades globales.**
## Puntos importantes / buenas prácticas

## Regla clave de dependencias

```
presentation → application → domain ← infra
```

El dominio **no depende de nada**.  
La infraestructura depende del dominio, nunca al revés.


## Puntos importantes / buenas prácticas

- **Fechas y zonas horarias**
  - Almacenar siempre fechas en **UTC** en la base de datos.
  - Convertir a zona local (ej. `America/Mexico_City`) solo en la capa de presentación.
  - Si se almacena en hora local, **documentar y mantener consistente**.

- **Seguridad de credenciales**
  - Nunca devolver el campo `password` (ni hashes) en responses.
  - El hash del password debe realizarse en el **usecase** (application), antes de persistir el usuario.
  - La capa `presentation` no debe conocer detalles de hashing.

- **Migraciones**
  - Usar **Alembic** para migraciones en producción.
  - `Base.metadata.create_all()` solo para desarrollo o SQLite local.
  - **Nunca** como estrategia principal en producción.

- **Separación de modelos**
  - Mantener separados:
    - DTOs (Pydantic) → `presentation/schemas`
    - Entidades de dominio → `domain/models`
    - Modelos ORM → `infra/db/models`
  - **Evitar dependencias cruzadas** para reducir acoplamiento.
- Otros settings importantes (por ejemplo):

## Variables de entorno relevantes (`.env`)

```
DATABASE_URL=postgresql://postgres:<PASSWORD>@<host>:5432/postgres
```

- Si la contraseña contiene caracteres especiales (`@`, `:`, `/`, etc.), debe **URL-encodearse**.
- Otros settings importantes:
  - `JWT_SECRET` (clave secreta para tokens)
  - `DEBUG` (modo debug)
  - `ACCESS_TOKEN_EXPIRE_MINUTES` (expiración de tokens)
- Todos se definen y cargan desde `src/core/config.py`.
```

## Cómo ejecutar en desarrollo

1. **Activar entorno virtual**
   - Linux/Mac:
     ```
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     .\venv\Scripts\Activate.ps1
     ```
   - Windows (cmd):
     ```
     .\venv\Scripts\activate.bat
     ```

2. **Instalar dependencias**
   ```
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   - Crear un archivo `.env` en la raíz del proyecto
   - Definir las variables necesarias (`DATABASE_URL`, JWT, etc.)

4. **Ejecutar la aplicación**
   ```
   uvicorn src.main:app --reload --log-level info
   ```

5. **Documentación interactiva**
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

> **¿Dudas o sugerencias?**
> Si tienes preguntas sobre la arquitectura, dependencias o cómo contribuir, revisa los comentarios en cada módulo o ponte en contacto con `@JoseManuel145` en github.
