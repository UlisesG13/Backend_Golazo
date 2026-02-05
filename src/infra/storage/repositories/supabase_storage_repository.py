from src.domain.ports.image_storage_port import ImagenStoragePort
from supabase import Client
from src.core.config import settings

class SupabaseStorageRepository(ImagenStoragePort):

    def __init__(self, client: Client):
        self.client = client
        self.bucket = settings.SUPABASE_BUCKET

    def upload(self, content: bytes, path: str) -> str:
        self.client.storage.from_(self.bucket).upload(
            path,
            content,
            {"content-type": "image/jpeg"}
        )
        return path

    def delete(self, path: str) -> None:
        self.client.storage.from_(self.bucket).remove([path])