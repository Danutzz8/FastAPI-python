# schemas.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class PostCreate(BaseModel):
    title: str
    content: str

class PostOut(BaseModel):
    id: int
    title: str
    content: str
    owner: UserOut
    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    text: str

class CommentOut(BaseModel):
    id: int
    text: str
    author: UserOut
    class Config:
        orm_mode = True
