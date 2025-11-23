from typing import List, Optional
from sqlalchemy.orm import Session
from src.domain.models.user_model import User
from src.domain.ports.user_port import UserService
from src.infra.db.models.user_table import Usuario   # SQLAlchemy model
from src.core.exceptions import NotFoundError

class UserRepository(UserService):
    def __init__(self, session: Session):
        self.session = session

    def _to_domain(self, r: Usuario) -> User:
        return User(
            usuario_id=r.usuario_id,
            nombre=r.nombre,
            email=r.email,
            password=r.password,
            telefono=r.telefono,
            direccion_id=r.direccion_id,
            rol=str(r.rol.value) if r.rol is not None else None,
            fecha_creacion=r.fecha_creacion,
        )

    def get_all(self) -> List[User]:
        rows = self.session.query(Usuario).all()
        return [self._to_domain(r) for r in rows]

    def get_by_id(self, usuario_id: str) -> Optional[User]:
        r = self.session.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
        if not r:
            return None
        return self._to_domain(r)

    def get_by_email(self, email: str) -> Optional[User]:
        r = self.session.query(Usuario).filter(Usuario.email == email).first()
        if not r:
            return None
        return self._to_domain(r)

    def create(self, user: User) -> User:
        model = Usuario(
            usuario_id=user.usuario_id,
            nombre=user.nombre,
            email=user.email,
            password=user.password,
            telefono=user.telefono,
            direccion_id=user.direccion_id,
            rol=user.rol,
        )
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return self._to_domain(model)

    def update(self, usuario_id: str, user: User) -> User:
        model = self.session.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")

        model.nombre = user.nombre
        model.email = user.email
        model.password = user.password
        model.telefono = user.telefono
        model.direccion_id = user.direccion_id
        model.rol = user.rol

        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return self._to_domain(model)

    def delete(self, usuario_id: str) -> None:
        model = self.session.query(Usuario).filter(Usuario.usuario_id == usuario_id).first()
        if not model:
            raise NotFoundError(f"Usuario {usuario_id} no existe")
        self.session.delete(model)
        self.session.commit()
