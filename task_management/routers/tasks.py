from uuid import uuid4
from fastapi import APIRouter, Depends
from dependencies import is_authenticated
from schemas.tasks import GetTask, CreateTask, UpdateTask
from schemas.task_history import TaskHistory
from db import get_db
from operations import tasks as tasks_ops
from operations import task_history as th_ops
from typing import List

tasks_router = APIRouter(prefix="/tasks")


@tasks_router.post("")
def create_task(data: CreateTask, current_user = Depends(is_authenticated), db = Depends(get_db)):
    return str(tasks_ops.create_task(data, current_user, db))



@tasks_router.get("")
def get_tasks(current_user = Depends(is_authenticated), db = Depends(get_db)) -> List[GetTask]:
    return tasks_ops.get_tasks(db)


@tasks_router.patch("/{task_id}")
def update_task(task_id: str, data: UpdateTask, current_user = Depends(is_authenticated), db = Depends(get_db)):
    tasks_ops.update_task(task_id, current_user, data, db)
    return

@tasks_router.get("/history/{task_id}")
def get_task_history(task_id: str, current_user = Depends(is_authenticated), db = Depends(get_db)) -> List[TaskHistory]:
    return th_ops.get_task_history(task_id, db)