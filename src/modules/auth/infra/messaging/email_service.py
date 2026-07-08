from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, make_msgid, formatdate
import aiosmtplib
from src.modules.auth.domain.ports import EmailPort
from src.core.config import settings
from src.core.exceptions import BadRequestError

class EmailService(EmailPort):

    def __init__(self):
        self.mail_username = settings.MAIL_USERNAME
        self.mail_password = settings.MAIL_PASSWORD

    @staticmethod
    def build_email_html(code: str, time: str) -> str:
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

    async def send_code(self, to_email: str, code: str):
        username = self.mail_username
        password = self.mail_password

        if not username or not password:
            raise BadRequestError("Faltan credenciales")

        html = self.build_email_html(
            code,
            str((datetime.now() + timedelta(minutes=15)).strftime("%H:%M:%S"))
        )

        msg = MIMEMultipart("alternative")
        msg['Message-ID'] = make_msgid()
        msg['Date'] = formatdate(localtime=True)
        msg["Subject"] = "Código de verificacion"
        msg["From"] = formataddr(("Soporte Golazo", username))
        msg["To"] = to_email

        msg.attach(MIMEText(html, "html"))

        await aiosmtplib.send(
            msg,
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            username=username,
            password=password,
        )
        return True