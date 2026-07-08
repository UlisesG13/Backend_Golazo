# Plan de Mejora — Backend Golazo

## 🔴 Crítico

- [ ] **H1 — Secrets expuestos en git**: `.env` y `src/core/golazo-b1c36-firebase*.json` están trackeados. Rotar todas las claves, `git rm --cached`, y actualizar `.gitignore` (`src/core/*.json`).
- [ ] **H2 — Passwords con SHA256**: `auth/infra/security/password_service.py` usa `hashlib.sha256`. Reemplazar con `bcrypt` (ya está en requirements).
- [ ] **H3 — EmailService bloquea event loop**: `send_code` declarado `async` en el port pero usa `smtplib` sync. Migrar a `aiosmtplib` o usar `asyncio.to_thread()`.
- [ ] **H4 — JWT secret débil**: Cambiar `SECRET_KEY="your_secret_key_here"` por un valor generado con `openssl rand -hex 32`.
- [ ] **H5 — Sin Alembic**: Inicializar `alembic`, configurar con el engine async, generar migración inicial.
- [ ] **H6 — Sin global exception handler**: Agregar `@app.exception_handler` en `main.py` para formatear errores consistentemente.
- [ ] **H7 — CORS mal configurado**: `"*"` + `allow_credentials=True` es inválido. Además `localhost: 5173` tiene espacio extra. Usar orígenes explícitos.
- [ ] **H8 — Cero tests**: Agregar tests unitarios (pytest) para domain models, use cases (mocks), y endpoints (TestClient).
- [ ] **H9 — print() en producción**: `ventas/app/pedido/create_pedido.py:129-144`. Reemplazar con logging.
- [ ] **H10 — Firebase key trackeada**: `src/core/golazo-b1c36-firebase-adminsdk-fbsvc-33611d463a.json` no está en `.gitignore` (falta `src/core/` prefix). Rotar la key y remover del historial.

> NOTAS: H1 no esta commiteados, H2, puedes modificar a ARGON2, H3 actualiza a async, H4 haz lo mejor que consideres, H5 haz lo que consideres mejor, H6 aagrega el global exception, H7 por ahora no hay origenes exactos por eso esta asi, H8 no hubo necesidad de tests, H9 esos prints se me escaparon y no hace falta logging, elimina los prints, H10 no esta trakeada

## 🟡 Medio

- [ ] **M1 — Supabase client sin singleton**: `core/supabase_config.py` crea un nuevo `Client` en cada llamada. Cachear a nivel de módulo.
- [ ] **M2 — GoogleOAuthService bloquea event loop**: Usa `requests` sync desde flujo async. Migrar a `httpx.AsyncClient`.
- [ ] **M3 — Settings sin validación**: Usar `pydantic-settings` (`BaseSettings`) en vez de `os.getenv()`.
- [ ] **M4 — Pool de conexiones sin tuning**: Agregar `pool_size=20`, `max_overflow=10`, `pool_recycle=3600` en `create_async_engine`.
- [ ] **M5 — InvalidToken importado mal**: `auth/infra/jwt/token_service.py:3` importa del paquete de two-factor, no de JWT. Usar `UnauthorizedError` de `exceptions.py`.
- [ ] **M6 — sync/async mismatch en verify_token**: `VerifyToken.execute` es `async` pero llama método sync. Simplificar.
- [ ] **M7 — _to_domain(None)**: `recovery_repository.py:36` llama `_to_domain(None)` cuando no hay registro. Agregar guarda.
- [ ] **M8 — Estilo mezclado en DTOs**: Unificar `Optional[int]` → `int | None`, `Config` → `model_config = ConfigDict(from_attributes=True)`.
- [ ] **M9 — __all__ con objetos**: `usuarios/application/usuario/__init__.py` usa clases en vez de strings en `__all__`.
- [ ] **M10 — DireccionDTO sin colonia**: Falta el campo `colonia: str` que sí existe en `DireccionTable` y `DireccionModel`.
- [ ] **M11 — Sin lifespan events**: Agregar `@asynccontextmanager lifespan` en `main.py` para inicializar Firebase y cerrar pool de conexiones.
- [ ] **M12 — Typo**: "Credenciales" → "Credenciales" en `login_user.py`.
- [ ] **M13 — Variable shadow**: `status` en `pedido_routes.py:39` shadowea el built-in. Renombrar a `estado`.
- [ ] **M14 — Sin structured logging**: Agregar middleware para request ID, timing, y logging estructurado (JSON).

> NOTAS: M1 usa singleton de supabase client, M2 migra a asuncclient, M3 usa pydantic-settings, M4 haz lo que mejor consideres, M5 corrige ese error de importacion, M6 corrige ese mimsmatch, M7 corrige eso, M8 usa optional, M9 se me hizo mas legible usando clases en lugar de strings pero veo que es innecesario ya que con la pura referencia del import se puede importar desde el exterior, M10 corrige ese dato faltante, M11 corrige eso, M12 corrige ese typo, M13 corrige ese shadow, M14 agrega ese logging del que hablas 

## 🟢 Bajo

- [ ] **L1**: `DireccionRequestDTO` duplica campos de `DireccionDTO` — usar herencia.
- [ ] **L2**: `numero_casa: int` debería ser `int | None` (columna nullable en DB).
- [ ] **L3**: Limpiar imports no usados restantes.
- [ ] **L4**: `.gitignore`: `**__pycache__/` no cubre `foo/__pycache__/`. Cambiar a `**/__pycache__/`.
- [ ] **L5**: `DeviceTokenTable.token: String(50)` muy corto para FCM tokens. Usar `Text` o `String(512)`.
- [ ] **L6**: Mezcla de PKs integer y UUID entre tablas (DireccionTable vs UserTable).
- [ ] **L7**: Sin rate limiting en endpoints de auth (`/login`, `/register`, `/recovery/*`).
- [ ] **L8**: Password sin validación (min_length, complejidad) en DTOs.
- [ ] **L9**: Varios endpoints retornan `None` en vez de usar `no_content_response()`.
- [ ] **L10**: `DireccionRepository.delete_direccion` traga silenciosamente not-found.

> NOTAS: L1 se me hace mas legible rapidamente duplicar campos, L2 corrige eso toma como nota que en DOMAIN se usa int | None y en los dtos/schemas se usa Optional, L3 limpia imports en todos los archivos, L4 corrige el gitignore, L5 corrige usando text, L6 corrige eso, L7 aplica rate limiting, L8 aplica validaciones, L9 corrige eso de None (no sabia que existia eso), L10 los deletes no deben revelar si existe o no, simplemente eliminarlo 
---

## ✅ Completado (Julio 2026)

- Migración sync → async SQLAlchemy (core, ports, repos, use cases, routes, security)
- Excepciones custom (NotFoundError, BadRequestError, ConflictError) en lugar de ValueError
- HTTP status codes (201 en POST, 204 en DELETE)
- Limpieza de imports no usados (ruff F401)
