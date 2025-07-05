from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env (if present)
load_dotenv()

# Connection URI (default: local MongoDB)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "todo_db"
COLLECTION_NAME = "tasks"

# Connect to MongoDB
_client = MongoClient(MONGO_URI)
_db = _client[DB_NAME]
tasks_collection = _db[COLLECTION_NAME]

# Function to check DB connection
def ping():
    _client.admin.command("ping")  # Will raise error if Mongo is unreachable

# Helper: current UTC timestamp
def now_utc():
    return datetime.utcnow()


if __name__ == "__main__":
    try:
        ping()
        print("✅ MongoDB connection successful.")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
