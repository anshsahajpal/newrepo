import datetime
from pydantic import BaseModel, UUID4


class TaskHistory(BaseModel):

    id: UUID4
    task_id: UUID4
    changed_by: UUID4  # User who made the change
    changed_at: datetime.datetime
    field_changed: str  # Name of the field that was changed
    old_value: str  # Old value before change
    new_value: str  # New value after change