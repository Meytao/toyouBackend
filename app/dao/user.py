from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import LoginRequest


async def login(db: AsyncSession, request: LoginRequest):
    result = await db.execute(select(User).where(User.username == request.username))
    user = result.scalar_one_or_none()
    return user
