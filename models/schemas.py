from typing import Annotated
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Annotated[str, None] = ""
    completed: Annotated[bool, None] = False
    
class TaskCreate(TaskBase):
    user_id: int


class Task(TaskCreate):
    id: int

    class Config:
        orm_mode = True
        
        
class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    tasks: list[Task] = []

    class Config:
        orm_mode = True
