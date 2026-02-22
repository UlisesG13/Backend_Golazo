from src.modules.auth.domain.ports import AuthPort, PasswordPort, TokenPort
from src.modules.auth.domain.models import AuthUser, TokenPayload
from datetime import datetime, timedelta, timezone

class LoginUser:

    def __init__(
        self,
        auth_repo: AuthPort,
        password_port: PasswordPort,
        token_port: TokenPort,
    ):
        self.auth_repo = auth_repo
        self.password_port = password_port
        self.token_port = token_port

    def execute(self, credentials: AuthUser):
        user = self.auth_repo.get_by_email(credentials.email)
        if not user:
            raise ValueError("Credenciales inválidas")
        if not self.password_port.verify(credentials.password, user.password):
            raise ValueError("Credenciales inválidas")

        data = TokenPayload(
            usuario_id=user.usuario_id,
            email=user.email,
            rol=user.rol,
            exp=datetime.now(timezone.utc) + timedelta(hours=1),
        )
        token = self.token_port.generate(data)
        return {
            "token": token,
            "usuario_id": user.usuario_id,
            "email": user.email,
            "rol": user.rol,
        }