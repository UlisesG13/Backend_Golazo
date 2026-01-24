
# Backend – Arquitectura y estructura de Golazo

Backend en Python usando **FastAPI + SQLAlchemy**, organizado por capas siguiendo principios de **Clean Architecture / Hexagonal**.  
El objetivo es separar claramente responsabilidades, proteger el dominio y desacoplar infraestructura.

---

## Árbol principal (resumido)

```
   .
   ├── requirements.txt        # Dependencias del proyecto (pip)
   ├── readme.md               # Documentación del proyecto
   ├── .gitignore              # Archivos/carpetas ignoradas por git
   ├── .env                    # Variables de entorno (NO versionar)
   ├── venv/                   # Entorno virtual local
   └── src
   ├── main.py            # Punto de entrada de la app (FastAPI)
   │
   ├── api/               # Capa de transporte (HTTP)
   │   ├── routers/       # Endpoints FastAPI (controllers)
   │   └── schemas/       # DTOs / Pydantic schemas (request/response)
   │
   ├── core/              # Configuración y utilidades transversales
   │   ├── config.py      # Carga de settings desde variables de entorno
   │   ├── exceptions.py  # Excepciones y errores estandarizados
   │   ├── logging.py     # Configuración de logging
   │   └── dependency_inyection/
   │       └── *.py       # Factories de dependencias (DI para FastAPI)
   │
   ├── domain/            # Núcleo del negocio (independiente de frameworks)
   │   ├── models/        # Entidades del dominio (dataclasses)
   │   └── ports/         # Interfaces (contratos) que usan los usecases
   │
   ├── infra/             # Implementaciones concretas
   │   └── db/
   │       ├── database.py# Engine, Session y conexión a la BD
   │       ├── models/    # Modelos ORM (SQLAlchemy) y enums
   │       └── repositories/
   │           └── *.py   # Implementaciones de los ports (persistencia)
   │
   └── usecases/          # Casos de uso / lógica de aplicación
      └── *.py            # Orquestación entre dominio y puertos
                          # Pendiente por separar por usecase

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
- Orquesta entidades del dominio y puertos
- No conoce FastAPI ni SQLAlchemy

### `domain/`
Capa más importante.
- Modela el negocio
- Define entidades y contratos
- No depende de ninguna otra capa

### `infra/`
Detalles técnicos.
- Base de datos
- ORM
- Servicios externos
Implementa los contratos definidos en `domain/ports`.

### `core/`
Soporte transversal.
- Configuración
- Logging
- Seguridad
- Inyección de dependencias

---

## Regla clave de dependencias

```

api → usecases → domain ← infra

```

El dominio no depende de nada.  
La infraestructura depende del dominio, nunca al revés.

---

## Puntos importantes / buenas prácticas

- **Fechas y zonas horarias**
  - Almacenar siempre fechas en **UTC** en la base de datos.
  - Convertir a zona local (por ejemplo `America/Mexico_City`) únicamente en la capa de presentación si es necesario.
  - Si se decide almacenar directamente en hora local, debe **documentarse claramente** y mantenerse consistente en todo el sistema.

- **Seguridad de credenciales**
  - Nunca devolver el campo `password` (ni hashes) en responses.
  - El hash del password debe realizarse en el **usecase**, antes de persistir el usuario.
  - La capa `api` no debe conocer detalles de hashing.

- **Migraciones**
  - Usar **Alembic** para manejar migraciones en entornos productivos.
  - `Base.metadata.create_all()` solo debe usarse como:
    - Soporte temporal en desarrollo
    - Fallback para SQLite local
  - Nunca como estrategia principal en producción.

- **Separación de modelos**
  - Mantener claramente separados:
    - DTOs (Pydantic) → `api/schemas`
    - Entidades de dominio → `domain/models`
    - Modelos ORM → `infra/db/models`
  - Evita dependencias cruzadas para reducir acoplamiento y facilitar cambios futuros.

---

## Variables de entorno relevantes (`.env`)

```

DATABASE_URL=postgresql://postgres:<PASSWORD>@<host>:5432/postgres

````

- Si la contraseña contiene caracteres especiales (`@`, `:`, `/`, etc.), debe **URL-encodearse**.
- Otros settings importantes (por ejemplo):
  - `JWT_SECRET`
  - `DEBUG`
  - `ACCESS_TOKEN_EXPIRE_MINUTES`
- Todos se definen y cargan desde `src/core/config.py`.

---

## Cómo ejecutar en desarrollo

1. **Activar entorno virtual**

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
