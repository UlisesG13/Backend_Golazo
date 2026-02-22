from src.modules.auth.domain.ports import GoogleOAuthPort, AuthPort, TokenPort
from src.modules.auth.domain.models import AuthUser, TokenPayload
from datetime import datetime, timezone
from uuid import uuid4

class LoginWithGoogle:

    def __init__(
        self,
        google_oauth: GoogleOAuthPort,
        user_repo: AuthPort,
        token_service: TokenPort,
    ):
        self.google_oauth = google_oauth
        self.user_repo = user_repo
        self.token_service = token_service

    def execute(self, code: str) -> str:

        tokens = self.google_oauth.exchange_code(code)
        user_info = self.google_oauth.verify_id_token(tokens["id_token"])

        google_id = user_info["sub"]
        email = user_info["email"]
        nombre = user_info.get("name", "")

        user = self.user_repo.get_by_google_id(google_id)

        if not user: # si no encuentra el usuario por google id
            existing = self.user_repo.get_by_email(email) #busca por email

            if existing: # si existe agrega su google_id
                self.user_repo.link_google(existing.usuario_id, google_id)
                user = existing
            else: # si no existe lo crea
                user = AuthUser(
                    usuario_id=str(uuid4()),
                    nombre=nombre,
                    email=email,
                    password=None,
                    rol="cliente",
                    telefono=None,
                    google_id=google_id,
                    is_authenticated=True,
                    fecha_creacion=datetime.now(timezone.utc),
                    fecha_eliminacion=None
                )
                user = self.user_repo.create(user)

        payload = TokenPayload(
            usuario_id=user.usuario_id,
            email=user.email,
            rol=user.rol,
            exp=...  # definido por tu TokenService
        )
        self.user_repo.verify_user(user.usuario_id)
        return self.token_service.generate(payload)