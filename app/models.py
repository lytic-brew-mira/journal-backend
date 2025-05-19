from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class JournalEntry(BaseModel):
    text: str
    created_at: Optional[datetime] = None
    ai_summary: Optional[str] = None
    tags: Optional[list[str]] = []
