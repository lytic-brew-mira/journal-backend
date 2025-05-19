from fastapi import APIRouter, Depends
from app.models import JournalEntry
from app.firestore import get_user_collection
from app.auth import get_user_id
from datetime import datetime

router = APIRouter()


@router.post("/")
def create_entry(entry: JournalEntry, user_id: str = Depends(get_user_id)):
    entry.created_at = datetime.utcnow()
    doc_ref = get_user_collection(user_id).document()
    doc_ref.set(entry.dict())
    return {"id": doc_ref.id, **entry.dict()}


@router.get("/")
def list_entries(user_id: str = Depends(get_user_id)):
    entries = get_user_collection(user_id).stream()
    return [{"id": e.id, **e.to_dict()} for e in entries]


@router.get("/{entry_id}")
def get_entry(entry_id: str, user_id: str = Depends(get_user_id)):
    doc = get_user_collection(user_id).document(entry_id).get()
    if not doc.exists:
        return {"error": "Not found"}
    return {"id": doc.id, **doc.to_dict()}
