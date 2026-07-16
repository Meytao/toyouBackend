from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.database import ensure_database_exists, create_tables
from app.config.settings import settings
from app.utils.init_data import init_all_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动前：检查并创建数据库和表
    await ensure_database_exists()
    await create_tables()
    # 初始化数据
    await init_all_data()
    yield
    # 关闭后（可清理资源）


app = FastAPI(
    title=settings.APP_NAME,
    debug=True,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World", "env": settings.APP_ENV, "debug": settings.DEBUG,
            "database_url": settings.DATABASE_URL}
