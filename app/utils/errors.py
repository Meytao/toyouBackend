"""全局异常处理:APIError / 校验失败 / 未捕获异常 -> 信封。"""
from __future__ import annotations

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.utils.response import APIError, fail


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(APIError)
    async def _api_err(request: Request, exc: APIError):
        return JSONResponse(status_code=exc.http_status, content=fail(exc.code, exc.message))

    @app.exception_handler(RequestValidationError)
    async def _val_err(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content=fail(1100, f"参数校验失败: {exc.errors()}"),
        )

    @app.exception_handler(Exception)
    async def _unhandled(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content=fail(-1, "internal error"))
