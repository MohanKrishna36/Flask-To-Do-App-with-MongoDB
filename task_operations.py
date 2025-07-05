"""
task_operations.py
All CRUD (Create, Read, Update, Delete) functions for the To‑Do app.
"""

from bson import ObjectId

from db import tasks_collection, now_utc
import utils  # we'll implement these helpers in utils.py


# ---------- CREATE ----------
from utils import get_current_time

def create_task(description, priority="Medium", status="Pending"):
    task = {
        "task": description,
        "priority": priority,
        "status": status,
        "created_at": get_current_time()
    }
    result = tasks_collection.insert_one(task)
    return result.inserted_id


# ---------- READ ----------
def fetch_all_tasks():
    """
    Fetch every task, oldest first, and return as a Python list.
    """
    return list(tasks_collection.find().sort("created_at", 1))


# ---------- UPDATE ----------
def update_task(task_id: str, *, description=None, priority=None, status=None):
    """
    Update fields on a task. Any argument left as None is ignored.
    Raises ValueError if the task isn’t found.
    """
    update_fields = {}

    if description is not None:
        utils.validate_description(description)
        update_fields["task"] = description.strip()

    if priority is not None:
        utils.validate_priority(priority)
        update_fields["priority"] = priority

    if status is not None:
        utils.validate_status(status)
        update_fields["status"] = status

    if not update_fields:
        raise ValueError("Nothing to update")

    update_fields["updated_at"] = now_utc()

    result = tasks_collection.update_one(
        {"_id": utils.parse_object_id(task_id)},
        {"$set": update_fields},
    )

    if result.matched_count == 0:
        raise ValueError("Task not found")


# ---------- DELETE ----------
def delete_task(task_id: str):
    """
    Delete a task by its _id string. Raises ValueError if not found.
    """
    result = tasks_collection.delete_one(
        {"_id": utils.parse_object_id(task_id)}
    )

    if result.deleted_count == 0:
        raise ValueError("Task not found")



def delete_task(task_id):
    result = tasks_collection.delete_one({"_id": task_id})
    return result.deleted_count

from bson import ObjectId

def get_task_by_id(task_id):
    return tasks_collection.find_one({"_id": ObjectId(task_id)})

def update_task(task_id, description, priority, status):
    update = {
        "task": description,
        "priority": priority,
        "status": status
    }
    return tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": update}
    )
