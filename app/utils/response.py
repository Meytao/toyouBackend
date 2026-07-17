"""统一响应信封工具。"""
from __future__ import annotations


class APIError(Exception):
    """业务异常。code 见 docs/superpowers/specs/2026-07-10-crud-design.md §7。"""

    def __init__(self, code: int, message: str, http_status: int = 400) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.http_status = http_status


def ok(data=None) -> dict:
    return {"code": 200, "message": "ok", "data": data}


def fail(code: int, message: str) -> dict:
    return {"code": code, "message": message, "data": None}
