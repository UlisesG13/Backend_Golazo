from src.modules.usuarios.infra.tables import UserTable
from src.modules.auth.domain.models import AuthUser
from src.modules.auth.domain.ports import AuthPort
from src.core.exceptions import NotFoundError
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from sqlalchemy import update
from typing import Optional


def _to_domain(obj: UserTable) -> AuthUser:
    return AuthUser(
        usuario_id=obj.usuario_id,
        nombre=obj.nombre,
        email=obj.email,
        password=obj.password,
        telefono=obj.telefono or "",
        rol=str(obj.rol.value) if obj.rol is not None else None,
        fecha_creacion=obj.fecha_creacion,
        google_id=obj.google_id,
        is_authenticated=obj.is_authenticated,
        fecha_eliminacion=obj.fecha_eliminacion
    )
class AuthRepository(AuthPort):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: AuthUser) -> AuthUser:
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
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return _to_domain(model)

    def get_by_id(self, usuario_id: str) -> Optional[AuthUser]:
        stmt = select(UserTable).where(UserTable.usuario_id == usuario_id)
        r = self.db.execute(stmt).scalar()
        if r is None:
            return None
        return _to_domain(r)

    def get_by_email(self, email: str) -> Optional[AuthUser]:
        stmt = select(UserTable).where(UserTable.email == email)
        r = self.db.execute(stmt).scalar_one_or_none()
        if r is None:
            return None
        return _to_domain(r)

    def get_by_google_id(self, google_id: str) -> Optional[AuthUser]:
        stmt = select(UserTable).where(UserTable.google_id == google_id)
        r = self.db.execute(stmt).scalar()
        if r is None:
            return None
        return _to_domain(r)


    def update_password(self, usuario_id: str, password_hash: str) -> None:
        stmt = (
            update(UserTable)
            .where(UserTable.usuario_id == usuario_id)
            .values(password=password_hash)
        )

        result = self.db.execute(stmt)

        if result.rowcount == 0:
            raise NotFoundError("User not found")

        self.db.commit()

    def verify_user(self, usuario_id: str) -> None:
        stmt = (
            update(UserTable)
            .where(UserTable.usuario_id == usuario_id)
            .values(is_authenticated=True)
        )
        result = self.db.execute(stmt)

        if result.rowcount == 0:
            raise NotFoundError("User not found")

        self.db.commit()

    def link_google(self, usuario_id: str, google_id: str) -> None:
        stmt = (
            update(UserTable)
            .where(UserTable.usuario_id == usuario_id)
            .values(google_id=google_id)
        )

        result = self.db.execute(stmt)

        if result.rowcount == 0:
            raise NotFoundError("User not found")

        self.db.commit()