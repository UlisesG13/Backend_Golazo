from src.modules.auth.domain.models import AuthUser
from src.modules.usuarios.domain.models import UserModel
from src.modules.usuarios.infra.tables import UserTable, Rol
from src.modules.usuarios.domain.ports import UserPort
from src.core.exceptions import NotFoundError
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone
from sqlalchemy import select


def _to_domain(r: UserTable) -> UserModel:
    return UserModel(
        usuario_id=r.usuario_id,
        nombre=r.nombre,
        email=r.email,
        telefono=r.telefono,
        rol=r.rol.value if r.rol else None,
        fecha_creacion=r.fecha_creacion,
        fecha_eliminacion=r.fecha_eliminacion,
    )

class UserRepository(UserPort):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[UserModel]:
        stmt = select(UserTable)
        rows = (await self.session.execute(stmt)).scalars().all()
        return [_to_domain(r) for r in rows]

    async def get_by_id(self, usuario_id: str) -> UserModel | None:
        stmt = (
            select(UserTable)
            .where(
                UserTable.usuario_id == usuario_id,
                UserTable.fecha_eliminacion.is_(None)
            )
        )
        r = (await self.session.execute(stmt)).scalar_one_or_none()
        return _to_domain(r) if r else None

    async def get_by_email(self, email: str) -> UserModel | None:
        stmt = (
            select(UserTable)
            .where(
                UserTable.email == email,
                UserTable.fecha_eliminacion.is_(None)
            )
        )
        r = (await self.session.execute(stmt)).scalar_one_or_none()

        return _to_domain(r) if r else None

    async def update(self, usuario_id: str, user: UserModel) -> UserModel:
        stmt = select(UserTable).where(UserTable.usuario_id == usuario_id)
        model = (await self.session.execute(stmt)).scalar_one_or_none()

        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")

        model.nombre = user.nombre
        model.telefono = user.telefono

        await self.session.commit()
        await self.session.refresh(model)

        return _to_domain(model)

    async def delete(self, usuario_id: str) -> None:
        model = (await self.session.execute(
            select(UserTable).filter(UserTable.usuario_id == usuario_id)
        )).scalar_one_or_none()
        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")
        await self.session.delete(model)
        await self.session.commit()

    async def anonymize_and_soft_delete(self, usuario_id: str) -> None:
        user = (await self.session.execute(
            select(UserTable).filter(UserTable.usuario_id == usuario_id)
        )).scalar_one_or_none()
        if not user:
            raise NotFoundError("Usuario no existe")

        user.nombre = "USUARIO ELIMINADO"
        user.email = f"deleted_{usuario_id}@deleted.local"
        user.telefono = None
        user.fecha_eliminacion = datetime.now(timezone.utc)

        await self.session.commit()

    async def create_admin(self, user: AuthUser) -> UserModel:
        model = UserTable(
            usuario_id=user.usuario_id,
            nombre=user.nombre,
            email=user.email,
            password=user.password,
            telefono=user.telefono or "",
            rol=user.rol,
            fecha_creacion=user.fecha_creacion,
            google_id=user.google_id,
            is_authenticated=user.is_authenticated,
            fecha_eliminacion=user.fecha_eliminacion
        )
        self.session.add(model)
        await self.session.commit()
        await self.session.refresh(model)
        return _to_domain(model)

    async def get_all_admins(self) -> list[UserModel]:
        stmt = select(UserTable).where(UserTable.rol == Rol.administrador.value)
        rows = (await self.session.execute(stmt)).scalars().all()
        return [_to_domain(r) for r in rows]
