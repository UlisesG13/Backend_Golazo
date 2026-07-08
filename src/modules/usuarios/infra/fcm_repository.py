from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.usuarios.domain.models import DeviceToken
from src.modules.usuarios.domain.ports import DeviceTokenPort
from src.modules.usuarios.infra.tables import DeviceTokenTable


def to_domain(r: DeviceTokenTable) -> DeviceToken:
    return DeviceToken(
        id=r.id,
        user_id=r.user_id,
        token=r.token,
        created_at=r.created_at
    )


class DeviceTokenRepository(DeviceTokenPort):
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def save(self, user_id: str, token: str) -> None:
        stmt = select(DeviceTokenTable).filter(DeviceTokenTable.token == token)
        existing = (await self.db.execute(stmt)).scalars().first()
        if existing:
            return
        new_token = DeviceTokenTable(
            user_id=user_id,
            token=token
        )

        self.db.add(new_token)
        await self.db.flush()
        await self.db.refresh(new_token)
        await self.db.commit()

    async def get_by_user(self, user_id: int) -> list[DeviceToken]:
        stmt = select(DeviceTokenTable).filter(DeviceTokenTable.user_id == user_id)
        rows = (await self.db.execute(stmt)).scalars().all()
        return [to_domain(r) for r in rows]

    async def get_all(self) -> list[DeviceToken]:
        stmt = select(DeviceTokenTable)
        rows = (await self.db.execute(stmt)).scalars().all()
        return [to_domain(r) for r in rows]

    async def delete(self, token: str) -> None:
        stmt = select(DeviceTokenTable).filter(DeviceTokenTable.token == token)
        r = (await self.db.execute(stmt)).scalars().first()

        if not r:
            return

        await self.db.delete(r)
        await self.db.commit()
