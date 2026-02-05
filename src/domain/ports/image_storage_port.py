from abc import ABC, abstractmethod

class ImagenStoragePort(ABC):

    @abstractmethod
    def upload(self, content: bytes, path: str) -> str:
        """Sube la imagen y retorna el path"""

    @abstractmethod
    def delete(self, path: str) -> None:
        """Elimina la imagen del bucket"""