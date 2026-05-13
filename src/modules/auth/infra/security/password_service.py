from src.modules.auth.domain.ports import PasswordPort
import hashlib

class PasswordService(PasswordPort):
    def hash(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def verify(self, plain: str, hash: str) -> bool:
        return hashlib.sha256(plain.encode()).hexdigest() == hash