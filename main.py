import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import user
from app.config.database import ensure_database_exists, create_tables
from app.config.settings import settings
from app.utils import response
from app.utils.init_data import init_all_data

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动前：检查并创建数据库和表
    logging.info("检查并创建数据库和表")
    await ensure_database_exists()
    logging.info("创建数据库和表")
    await create_tables()
    yield ()
    # 初始化数据
    logging.info("初始化系统数据")
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

# 注册认证路由
app.include_router(user.router)


@app.get("/")
async def root():
    return response.ok({"message": "Hello World", "env": settings.APP_ENV, "debug": settings.DEBUG,
                        "database_url": settings.DATABASE_URL})
