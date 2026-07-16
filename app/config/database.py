import importlib
import pkgutil
from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app import models
from app.config.settings import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=settings.DEBUG,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

Base = declarative_base()


async def ensure_database_exists():
    """检查数据库是否存在，不存在则创建"""
    tmp_engine = create_async_engine(settings.DATABASE_URL_BASE)
    try:
        async with tmp_engine.connect() as conn:
            await conn.execute(text(
                f"CREATE DATABASE IF NOT EXISTS `{settings.DB_NAME}` "
                f"DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci"
            ))
            await conn.commit()
    finally:
        await tmp_engine.dispose()


async def create_tables():
    """创建所有表(已存在则跳过)。自动扫描 app.models 下所有模块,避免漏建表。"""
    # 自动 import 所有模型子模块,确保它们注册到 Base.metadata
    for module_info in pkgutil.iter_modules(models.__path__):
        module_name = module_info.name
        if module_name.startswith("_"):
            continue
        importlib.import_module(f"app.models.{module_name}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
