from src.modules.auth.domain.ports import AuthPort, PasswordPort, TokenPort
from src.modules.auth.domain.models import AuthUser, TokenPayload
from src.modules.auth.presentation.schemas import UserRegister
from datetime import datetime, timedelta, timezone
from src.modules.usuarios.infra.tables import Rol
from uuid import uuid4
from src.core.exceptions import ConflictError

class CreateAdmin:

    def __init__(
        self,
        auth_repo: AuthPort,
        password_port: PasswordPort,
        token_port: TokenPort,
    ):
        self.auth_repo = auth_repo
        self.password_repo = password_port
        self.token_repo = token_port

    async def execute(self, user: UserRegister):
        existing = await self.auth_repo.get_by_email(user.email)
        if existing:
            raise ConflictError("Email already registered")

        hashed = self.password_repo.hash(user.password)

        model = AuthUser(
            usuario_id=str(uuid4()),
            nombre=user.nombre,
            email=user.email,
            rol=Rol.administrador.value,
            fecha_creacion=datetime.now(timezone.utc),
            is_authenticated=True,
            password=hashed,
            telefono="",
            google_id=None,
        )

        user_created = await self.auth_repo.create(model)

        payload = TokenPayload(
            usuario_id=user_created.usuario_id,
            email=user_created.email,
            rol=user_created.rol,
            exp=datetime.now(timezone.utc) + timedelta(minutes=15),
        )

        token = self.token_repo.generate(payload)

        return {
            "token": token,
            "usuario_id": user_created.usuario_id,
            "email": user_created.email,
            "rol": user_created.rol,
        }
