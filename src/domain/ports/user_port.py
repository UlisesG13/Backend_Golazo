#interface
from abc import ABC, abstractmethod
import datetime
from typing import List, Optional
from src.domain.models.user_model import UserModel

class UserPort(ABC):
    @abstractmethod
    def get_all(self) -> List[UserModel]:
        """Lista todos los usuarios (solo para debug/testing)"""

    @abstractmethod
    def get_by_id(self, usuario_id: str) -> Optional[UserModel]:
        """Obtiene un usuario por su ID"""

    @abstractmethod
    def get_by_google_id(self, google_id: str) -> Optional[UserModel]:
        """Obtiene un usuario por su ID de Google (para auth Google)"""

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UserModel]:
        """Obtiene un usuario por su email (para signin)"""

    @abstractmethod
    def create(self, user: UserModel) -> UserModel:
        """Registra un usuario nuevo (para signup)"""

    @abstractmethod
    def update(self, usuario_id: str, user: UserModel) -> UserModel:
        """Actualiza datos del usuario"""

    @abstractmethod
    def delete(self, usuario_id: str) -> None:
        """Elimina un usuario"""
    
    @abstractmethod
    def anonymize_and_soft_delete(self, usuario_id: str, fecha_eliminacion: datetime) -> None:
        """Elimina lógicamente un usuario"""

    @abstractmethod
    def reset_password(self, usuario_id: str, new_password: str) -> None:
        """Resetea la contraseña del usuario"""

    @abstractmethod
    def update_authentication(self, usuario_id: str, is_authenticated: bool) -> None:
        """Actualiza el estado de autenticación del usuario"""