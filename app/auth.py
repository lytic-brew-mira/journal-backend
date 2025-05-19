from fastapi import Header, HTTPException


def get_user_id(x_user_id: str = Header(...)) -> str:
    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing user ID header")
    return x_user_id
