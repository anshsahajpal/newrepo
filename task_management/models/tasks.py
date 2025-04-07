from sqlalchemy import Column, UUID, String, DATETIME
from task_management.db import Base
import uuid
from datetime import datetime


class Tasks(Base):
    __tablename__ = "Tasks"

    id = Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4)
    title = Column(String)
    description = Column(String)
    created = Column(DATETIME)
    updated = Column(DATETIME, default=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    assigned_to = Column(UUID(as_uuid=True), nullable=False)
    state = Column(String)
    priority = Column(String)



