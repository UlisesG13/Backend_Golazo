from __future__ import annotations

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

class UserCreateDTO(BaseModel):
	"""Payload para crear un usuario."""

	nombre: str = Field(..., example="Juan Pérez")
	email: EmailStr = Field(..., example="juan@example.com")
	password: str = Field(..., min_length=6, example="secreto123")


class UserUpdateDTO(BaseModel):
	"""Payload para actualizar un usuario (todos campos opcionales)."""

	nombre: Optional[str] = Field(None, example="Juan Pérez")
	password: Optional[str] = Field(None, min_length=6, example="nuevo123")
	telefono: Optional[str] = Field(None, example="5512345678")


class UserDTO(BaseModel):
	"""Representación pública de un usuario para respuestas API."""

	usuario_id: str
	nombre: str
	email: EmailStr
	telefono: Optional[str]
	rol: Optional[str]
	fecha_creacion: datetime
	is_authenticated: bool | None = False
	google_id: Optional[str] | None = None
	password: Optional[str] | None = None
	fecha_eliminacion: Optional[datetime] | None = None
	
	class Config:
		from_attributes = True

class UserLoginDTO(BaseModel):
    """Payload para login de usuario."""

    email: EmailStr = Field(..., example="juan@example.com")
    password: str = Field(..., min_length=6, example="secreto123")

class TokenUserDTO(BaseModel):
    usuario_id: str
    email: str
    rol: str

class LoginResponseDTO(BaseModel):
    token: str
    usuario_id: str
    email: str
    rol: str

__all__ = ["UserCreateDTO", "UserUpdateDTO", "UserDTO", "UserLoginDTO", "LoginResponseDTO", "TokenUserDTO"]
