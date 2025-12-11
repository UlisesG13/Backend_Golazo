import os
import hashlib
import secrets
import string
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, make_msgid, formatdate
import smtplib
from typing import List
from src.domain.models.user_model import UserModel
from src.domain.ports.user_port import UserService
from src.core.config import settings

verification_store = {}

class UserUsecases:
    def __init__(self, repo: UserService):
        self.repo = repo
        self.mail_username = settings.MAIL_USERNAME
        self.mail_password = settings.MAIL_PASSWORD

    def list_users(self) -> List[UserModel]:
        return self.repo.get_all()

    def get_user_by_id(self, usuario_id: str) -> UserModel:
        user = self.repo.get_by_id(usuario_id)
        if not user:
            raise ValueError(f"Usuario con ID {usuario_id} no encontrado")
        return user

    def get_user_by_email(self, email: str) -> UserModel:
        user = self.repo.get_by_email(email)
        if not user:
            raise ValueError(f"Usuario con email {email} no encontrado")
        return user

    def create_user(self, user: UserModel) -> UserModel:
        user.password = self.hash_password(user.password)
        return self.repo.create(user)

    def update_user(self, usuario_id: str, user: UserModel) -> UserModel:
        return self.repo.update(usuario_id, user)

    def delete_user(self, usuario_id: str) -> None:
        self.repo.delete(usuario_id)

    def login(self, credentials: UserModel) -> UserModel:
        user = self.repo.get_by_email(credentials.email)
        if not user:
            raise ValueError("Credenciales inválidas")
        if not self.verify_password(credentials.password, user.password):
            raise ValueError("Credenciales inválidas")
        return user

    def generate_code(self, user_id: str) -> dict:
        charset = string.digits
        code = ''.join(secrets.choice(charset) for _ in range(6))
        expires_at = datetime.now() + timedelta(minutes=15)

        hashed = hashlib.sha256(code.encode()).hexdigest()

        verification_store[user_id] = {
            "code": hashed,
            "expires_at": expires_at
        }

        return {
            "code": code,
            "expires_at": expires_at
        }

    def is_code_valid(self, user_id: str, user_code: str) -> bool:
        data = verification_store.get(user_id)
        if not data:
            return False

        hashed_input = hashlib.sha256(user_code.encode()).hexdigest()
        if hashed_input != data["code"]:
            return False

        if datetime.now() > data["expires_at"]:
            return False

        verification_store.pop(user_id, None)
        return True

    def reset_password(self, usuario_id: str, new_password: str) -> UserModel:
        password = self.hash_password(new_password)
        return self.repo.reset_password(usuario_id, password)

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return hashlib.sha256(plain_password.encode()).hexdigest() == hashed_password
    
    def build_email_html(self, code: str, time: str) -> str:
        return f"""
        <html>
            <body style="font-family: Arial; padding: 20px;">
                <h2 style="color: #1a73e8;">Recuperación de contraseña</h2>
                <p>Usa este código para continuar:</p>
                <div style="
                    font-size: 32px;
                    font-weight: bold;
                    background: #f5f5f5;
                    padding: 15px;
                    width: fit-content;
                    border-radius: 8px;
                    border: 1px solid #ddd;">
                    {code}
                </div>
                <p>Vence a las {time}...</p>
            </body>
        </html>
        """

    def send_recovery_email(self, to_email: str, code: str):
        mail_username = self.mail_username
        mail_password = self.mail_password

        if not mail_username or not mail_password:
            raise ValueError("Faltan credenciales")

        html = self.build_email_html(
            code,
            (datetime.now() + timedelta(minutes=15)).strftime("%I:%M %p")
        )

        msg = MIMEMultipart("alternative")
        msg['Message-ID'] = make_msgid()
        msg['Date'] = formatdate(localtime=True)
        msg["Subject"] = "Código de recuperación"
        msg["From"] = formataddr(("Soporte Golazo", mail_username))
        msg["To"] = to_email

        msg.attach(MIMEText(html, "html"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(mail_username, mail_password)
            server.sendmail(mail_username, to_email, msg.as_string())
