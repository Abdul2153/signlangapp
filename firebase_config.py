import firebase_admin
from firebase_admin import credentials, firestore
import os

# Path to the service account key
cred_path = os.path.join(os.path.dirname(__file__), "firebase_config.json")

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Firestore database
db = firestore.client()
