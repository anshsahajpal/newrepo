from uuid import uuid4
from fastapi import APIRouter, Depends
import redis
from dependencies import is_authenticated
from schemas.tasks import GetTask, CreateTask, UpdateTask
from schemas.task_history import TaskHistory
from db import get_db
from operations import tasks as tasks_ops
from operations import task_history as th_ops
from typing import List
from shared.redis_pubsub import RedisPubsub

tasks_router = APIRouter(prefix="/tasks")

redispubsub = RedisPubsub(host="redis", port=6379, channel="notifications")

@tasks_router.post("")
def create_task(data: CreateTask, current_user = Depends(is_authenticated), db = Depends(get_db)):
    print("Creating task")
    redispubsub.publish({
        "message": "Task "+ str(data.title) + " created by " + str(current_user)
    })
    return str(tasks_ops.create_task(data, current_user, db))



@tasks_router.get("")
def get_tasks(current_user = Depends(is_authenticated), db = Depends(get_db)) -> List[GetTask]:
    return tasks_ops.get_tasks(db)


@tasks_router.patch("/{task_id}")
def update_task(task_id: str, data: UpdateTask, current_user = Depends(is_authenticated), db = Depends(get_db)):
    tasks_ops.update_task(task_id, current_user, data, db)
    redispubsub.publish({
        "message": "Task "+ str(data.title) + " updated by " + str(current_user)
    })
    return

@tasks_router.get("/history/{task_id}")
def get_task_history(task_id: str, current_user = Depends(is_authenticated), db = Depends(get_db)) -> List[TaskHistory]:
    return th_ops.get_task_history(task_id, db)