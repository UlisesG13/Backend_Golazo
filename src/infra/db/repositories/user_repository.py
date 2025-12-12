from datetime import datetime
import secrets
from typing import List, Optional
from zoneinfo import ZoneInfo
from sqlalchemy.orm import Session
from src.domain.models.user_model import UserModel
from src.domain.ports.user_port import UserService
from src.infra.db.models.user_table import UserTable   # SQLAlchemy model
from src.core.exceptions import NotFoundError

class UserRepository(UserService):
    def __init__(self, session: Session):
        self.session = session

    def _to_domain(self, r: UserTable) -> UserModel:
        return UserModel(
            usuario_id=r.usuario_id,
            nombre=r.nombre,
            email=r.email,
            password=r.password,
            telefono=r.telefono,
            direccion_id=r.direccion_id,
            rol=str(r.rol.value) if r.rol is not None else None,
            fecha_creacion=r.fecha_creacion,
            is_authenticated=r.is_authenticated,
        )

    def get_all(self) -> List[UserModel]:
        rows = self.session.query(UserTable).all()
        return [self._to_domain(r) for r in rows]

    def get_by_id(self, usuario_id: str) -> Optional[UserModel]:
        r = self.session.query(UserTable).filter(UserTable.usuario_id == usuario_id).first()
        if not r:
            return None
        return self._to_domain(r)

    def get_by_email(self, email: str) -> Optional[UserModel]:
        r = self.session.query(UserTable).filter(UserTable.email == email).first()
        if not r:
            return None
        return self._to_domain(r)

    def create(self, user: UserModel) -> UserModel:
        id = secrets.token_hex(16)
        if user.direccion_id is None or user.direccion_id == "" or user.direccion_id == 0:
            user.direccion_id = None
        fecha = datetime.now()
        if user.telefono is None or user.telefono == "" or user.telefono == 0:
            user.telefono = ""
        model = UserTable(
            usuario_id=id,
            nombre=user.nombre,
            email=user.email,
            password=user.password,
            telefono=user.telefono,
            direccion_id=user.direccion_id,
            rol=user.rol,
            fecha_creacion=fecha,
        )
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return self._to_domain(model)

    def update(self, usuario_id: str, user: UserModel) -> UserModel:
        model = self.session.query(UserTable).filter(UserTable.usuario_id == usuario_id).first()
        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")

        model.nombre = user.nombre
        model.email = user.email
        model.password = user.password
        model.telefono = user.telefono
        model.direccion_id = user.direccion_id
        model.rol = user.rol
        model.is_authenticated = user.is_authenticated
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return self._to_domain(model)

    def delete(self, usuario_id: str) -> None:
        model = self.session.query(UserTable).filter(UserTable.usuario_id == usuario_id).first()
        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")
        self.session.delete(model)
        self.session.commit()

    def reset_password(self, usuario_id: str, new_password: str) -> None:
        model = self.session.query(UserTable).filter(UserTable.usuario_id == usuario_id).first()
        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")
        model.password = new_password
        self.session.add(model)
        self.session.commit()