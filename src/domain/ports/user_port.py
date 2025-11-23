#interface
from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.models.user_model import User

class UserService(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        """Lista todos los usuarios (solo para debug/testing)"""

    @abstractmethod
    def get_by_id(self, usuario_id: str) -> Optional[User]:
        """Obtiene un usuario por su ID"""

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        """Obtiene un usuario por su email (para signin)"""

    @abstractmethod
    def create(self, user: User) -> User:
        """Registra un usuario nuevo (para signup)"""

    @abstractmethod
    def update(self, usuario_id: str, user: User) -> User:
        """Actualiza datos del usuario"""

    @abstractmethod
    def delete(self, usuario_id: str) -> None:
        """Elimina un usuario"""