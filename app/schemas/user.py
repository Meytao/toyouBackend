from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    id: int
    username: str
    display_name: str | None = None
    avatar: str | None = None
    email: str | None = None
    role: str

    class Config:
        from_attributes = True


class CreateUserRequest(BaseModel):
    username: str
    password: str
