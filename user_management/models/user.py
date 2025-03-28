import uuid
from user_management.db import Base
from sqlalchemy import Column, String, UUID


class User(Base):
    __tablename__ = "User"
    id = Column(UUID(as_uuid=True), primary_key=True, default= uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    email = Column(String,nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
