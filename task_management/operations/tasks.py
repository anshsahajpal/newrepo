from models.tasks import Tasks
from sqlalchemy.orm import Session
import uuid
from schemas.tasks import CreateTask, UpdateTask
from datetime import datetime
from . import task_history


def create_task(data: CreateTask, user_id, db: Session)-> uuid.UUID:
    task = Tasks(id = uuid.uuid4(), title=data.title, description=data.description, created=datetime.utcnow(), updated = datetime.utcnow(),
                 created_by = uuid.UUID(user_id), assigned_to = uuid.UUID(user_id), state=data.state, priority=data.priority)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task.id


def get_tasks(db: Session):
    return db.query(Tasks).all()


def update_task(task_id,user_id, data: UpdateTask, db: Session):
    task = db.query(Tasks).filter(Tasks.id == uuid.UUID(task_id)).first()
    if data.title:
        task_history.add_task_history(task_id, user_id, "title", task.title, data.title, db)
        task.title = data.title
    if data.description:
        task_history.add_task_history(task_id, user_id, "description", task.description, data.description, db)
        task.description = data.description
    if data.assigned_to:
        task_history.add_task_history(task_id, user_id, "assignee", task.assigned_to, data.assigned_to, db)
        task.assigned_to = uuid.UUID(data.assigned_to)
    if data.state:
        task_history.add_task_history(task_id, user_id, "state", task.state, data.state, db)
        task.state = data.state
    if data.priority:
        task_history.add_task_history(task_id, user_id, "priority", task.priority, data.priority, db)
        task.priority = data.priority
    task.updated = datetime.utcnow()
    db.commit()
    return