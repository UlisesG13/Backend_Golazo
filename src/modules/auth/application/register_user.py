from src.modules.auth.domain.ports import AuthPort, PasswordPort, TokenPort
from src.modules.auth.domain.models import AuthUser, TokenPayload
from datetime import datetime, timedelta, timezone
from uuid import uuid4

class RegisterUser:

    def __init__(
        self,
        auth_repo: AuthPort,
        password_port: PasswordPort,
        token_port: TokenPort,
    ):
        self.auth_repo = auth_repo
        self.password_repo = password_port
        self.token_repo = token_port

    def execute(self, user: AuthUser):
        existing = self.auth_repo.get_by_email(user.email)
        if existing:
            raise ValueError("Email already registered")

        hashed = self.password_repo.hash(user.password)

        model = AuthUser(
            usuario_id=str(uuid4()),
            nombre=user.nombre,
            email=user.email,
            rol="cliente",
            fecha_creacion=datetime.now(timezone.utc),
            is_authenticated=False,
            password=hashed,
            telefono="",
            google_id=None,
        )

        user_created = self.auth_repo.create(model)

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