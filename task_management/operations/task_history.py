from models.task_history import TaskHistory
from sqlalchemy.orm import Session
import uuid
from datetime import datetime


def add_task_history(task_id, user_id, field, old, new, db: Session):
    th = TaskHistory(id = uuid.uuid4(), task_id= uuid.UUID(task_id), changed_by=uuid.UUID(user_id), changed_at = datetime.utcnow(), field_changed = field, old_value = old, new_value = new)
    db.add(th)
    db.commit()
    db.refresh(th)
    return

def get_task_history(task_id, db: Session):
    return db.query(TaskHistory).filter(TaskHistory.task_id == uuid.UUID(task_id)).order_by(TaskHistory.changed_at).all()

