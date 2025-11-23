# Golazo - Backend

Descripción breve
- Backend en Python (FastAPI + SQLAlchemy). Organización por capas: api, usecases, domain, infra, core.

Árbol principal (resumido) y qué va en cada carpeta
.
├── requirements.txt                # Dependencias del proyecto (pip)
├── readme.md                       # Documentación (este archivo)
├── .gitignore                      # Archivos/carpetas ignoradas por git
├── .env                            # Variables de entorno (no subir a git)
├── venv/                           # Entorno virtual (local/dev)
└── src
    ├── main.py                     # Punto de entrada (instancia FastAPI, incluye routers)
    ├── api                          # Capa HTTP
    │   ├── routers/                 # FastAPI routers: definición de endpoints
    │   └── schemas/                 # Pydantic schemas / DTOs (validación y respuestas)
    │
    ├── core                         # Config y utilidades transversales
    │   ├── config.py                # Carga de settings desde .env / env vars
    │   ├── exceptions.py            # Helpers y excepciones HTTP estandarizadas
    │   ├── logging.py               # Configuración de logging de la app
    │   └── dependency_inyection/    # Factories / dependencias para FastAPI (DI)
    │
    ├── domain                       # Lógica de negocio pura
    │   ├── models/                  # Entidades del dominio (dataclasses / objetos)
    │   └── ports/                   # Interfaces (repositorios / servicios) usadas por usecases
    │
    ├── infra                        # Implementaciones de infraestructura
    │   └── db
    │       ├── database.py          # Engine, Session y fallback dev (SQLite)
    │       ├── models/              # Modelos ORM (SQLAlchemy) y enums
    │       └── repositories/        # Implementaciones concretas de ports (persistencia)
    │
    └── usecases/                    # Casos de uso / orquestación de la lógica (services)

Qué va en cada capa (resumen práctico)
- api/routers: recibir request, validar con Pydantic (dtos), inyectar dependencias, devolver respuestas HTTP. No lógica de negocio.
- api/dtos (schemas): Pydantic models para request y response. Actúan como DTOs entre cliente y backend.
- usecases: orquestan la lógica de negocio, aplican reglas, llaman a repositorios, gestionan transacciones cuando corresponde.
- domain/models: entidades puras y tipos del dominio (sin dependencias infra).
- domain/ports: interfaces que describen lo que necesita el dominio (p. ej. UserRepository).
- infra/db/models: tablas y mapeos ORM (SQLAlchemy). No lógica de negocio aquí.
- infra/db/repositories: implementan las interfaces (ports) y convierten ORM ↔ domain.
- core: configuración, logging, manejo centralizado de excepciones y DI.

Puntos importantes / buenas prácticas
- Almacenar fechas en UTC en la BD y convertir a zona local (p. ej. America/Mexico_City) en la capa de presentación si lo necesitas. Si decidiste guardar en hora de México, documenta y sé consistente.  
- No devolver password en responses; hash de password en usecase antes de persistir.  
- Usar Alembic para migraciones en producción. `Base.metadata.create_all()` sólo para desarrollo temporal (o fallback SQLite).  
- Mantener DTOs (Pydantic) separados de modelos ORM y de domain para evitar acoplamientos indebidos.

Variables de entorno relevantes (.env)
- DATABASE_URL=postgresql://postgres:<PASSWORD>@<host>:5432/postgres
  - Si la contraseña tiene caracteres especiales, url-encodearla.
- Otros settings (JWT_SECRET, DEBUG, etc.) se definen en src/core/config.py.

Cómo ejecutar en desarrollo
1. Activar virtualenv:
   - Windows (PowerShell): .\venv\Scripts\Activate.ps1
   - Windows (cmd): .\venv\Scripts\activate.bat
2. Instalar dependencias:
   pip install -r requirements.txt
3. Exportar .env o crear un archivo .env en la raíz con las variables necesarias.
4. Ejecutar:
   uvicorn src.main:app --reload --log-level info
5. Docs interactivos: http://127.0.0.1:8000/docs
