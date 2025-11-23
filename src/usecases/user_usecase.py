from typing import List
from src.domain.models.user_model import User
from src.domain.ports.user_port import UserService

class UserUsecases:
    def __init__(self, repo: UserService):
        self.repo = repo

    def list_users(self) -> List[User]:
        return self.repo.get_all()

    def get_user_by_id(self, usuario_id: str) -> User:
        user = self.repo.get_by_id(usuario_id)
        if not user:
            raise ValueError(f"Usuario con ID {usuario_id} no encontrado")
        return user
    
    def get_user_by_email(self, email: str) -> User:
        user = self.repo.get_by_email(email)
        if not user:
            raise ValueError(f"Usuario con email {email} no encontrado")
        return user
    
    def create_user(self, user: User) -> User:
        return self.repo.create(user)
    
    def update_user(self, usuario_id: str, user: User) -> User:
        return self.repo.update(usuario_id, user)
    
    def delete_user(self, usuario_id: str) -> None:
        self.repo.delete(usuario_id)
        
    def login(self, user: User) -> User:
        user = self.repo.get_by_email(user.email)
        if not user or user.password != user.password:
            raise ValueError("Credenciales inválidas")
        return user
    
    def reset_password(self, email: str, new_password: str) -> User:
        user = self.repo.get_by_email(email)
        if not user:
            raise ValueError(f"Usuario con email {email} no encontrado")
        user.password = new_password
        return self.repo.update(user.usuario_id, user)