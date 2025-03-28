from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    title: str
    description: str
    state: str
    priority: str


class CreateTask(Task):
    assigned_to: UUID4

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    state: Optional[str] = None
    priority: Optional[str] = None
    assigned_to: Optional[UUID4] = None

class GetTask(Task):
    id: UUID4
    created: datetime
    updated: datetime
    created_by:  UUID4
    assigned_to: UUID4
