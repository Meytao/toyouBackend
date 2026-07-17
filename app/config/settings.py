import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


def get_env():
    env = os.getenv("APP_ENV", "dev")
    env_files = {
        "dev": ".env.dev",
        "prod": ".env.prod",
    }
    return env_files.get(env, ".env.dev")


load_dotenv(get_env())


class Settings(BaseSettings):
    APP_ENV: str = "dev"
    APP_NAME: str = "toyou-backend"
    DEBUG: bool = False

    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASSWORD: str = ""
    DB_NAME: str = "toyou"

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    JWT_SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7天

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset=utf8mb4"

    @property
    def DATABASE_URL_BASE(self) -> str:
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/?charset=utf8mb4"

    class Config:
        env_file = get_env()


settings = Settings()
