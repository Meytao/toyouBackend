from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import get_db
from app.models.user import User
from app.schemas.user import LoginRequest, TokenResponse, UserResponse, CreateUserRequest
from app.utils.jwt import create_access_token
from app.utils.security import get_hash_password, verify_password

router = APIRouter(prefix="/api/user", tags=["user"])


@router.post("/login", response_model=TokenResponse)
async def login(request: LoginRequest, db: AsyncSession = Depends(get_db)):
    """用户登录，返回 JWT Token"""
    # 1. 查询用户
    result = await db.execute(select(User).where(User.username == request.username))
    user = result.scalar_one_or_none()

    if not user or verify_password(request.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
        )

    # 2. 用用户身份信息生成 token
    token_data = {
        "user_id": user.id,
        "username": user.username,
        "role": user.role,
    }
    access_token = create_access_token(data=token_data)

    return TokenResponse(access_token=access_token)


@router.get("/info", response_model=UserResponse)
async def get_current_user(token: str, db: AsyncSession = Depends(get_db)):
    """获取当前登录用户信息"""
    from app.utils.jwt import verify_token

    # 验证 token 并获取用户信息
    payload = verify_token(token)
    user_id = payload.get("user_id")

    # 查询数据库获取完整用户信息
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在",
        )

    return user


@router.post("/register", response_model=UserResponse)
async def register(request: CreateUserRequest, db: AsyncSession = Depends(get_db)):
    """用户注册"""
    # 1. 检查用户名是否存在
    result = await db.execute(select(User).where(User.username == request.username))
    user = result.scalar_one_or_none()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名已存在",
        )
    else:
        user = User(
            username=request.username,
            password_hash=get_hash_password(request.password),
        )
        db.add(user)
        await db.commit()
        return user
