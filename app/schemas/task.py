from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    status: str = "todo"
    priority: str = "low"

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str | None
    status: str
    priority: str
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True