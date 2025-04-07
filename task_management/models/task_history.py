from sqlalchemy import Column, UUID, String, DATETIME, ForeignKey, Text
from task_management.db import Base
import uuid
from datetime import datetime


class TaskHistory(Base):
    __tablename__ = "TaskHistory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    task_id = Column(UUID(as_uuid=True), ForeignKey("Tasks.id"), nullable=False)
    changed_by = Column(UUID(as_uuid=True), nullable=False)  # User who made the change
    changed_at = Column(DATETIME, default=datetime.utcnow)  # Timestamp of change
    field_changed = Column(String, nullable=False)  # Name of the field that was changed
    old_value = Column(Text, nullable=True)  # Old value before change
    new_value = Column(Text, nullable=True)  # New value after change