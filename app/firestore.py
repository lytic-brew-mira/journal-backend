import os
from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT")
db = firestore.Client(project=PROJECT_ID)


def get_user_collection(user_id: str):
    return db.collection("users").document(user_id).collection("journals")
