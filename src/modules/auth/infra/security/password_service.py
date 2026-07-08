from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from src.modules.auth.domain.ports import PasswordPort

_hasher = PasswordHasher(
    time_cost=2,
    memory_cost=102400,
    parallelism=8,
    hash_len=32,
    salt_len=16,
)

class PasswordService(PasswordPort):
    def hash(self, password: str) -> str:
        return _hasher.hash(password)

    def verify(self, plain: str, hash: str) -> bool:
        try:
            return _hasher.verify(hash, plain)
        except VerifyMismatchError:
            return False