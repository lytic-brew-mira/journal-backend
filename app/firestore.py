from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv()

db = firestore.Client(database="lytic-brew-mira-development-db")


def get_user_collection(user_id: str):
    return db.collection("users").document(user_id).collection("journals")
