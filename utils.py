"""
utils.py
Validation helpers and pretty‑table formatter for the To‑Do app.
"""

from db import tasks_collection
from bson import ObjectId
from tabulate import tabulate

# --------- Constants ---------
VALID_PRIORITIES = {"High", "Medium", "Low"}
VALID_STATUSES   = {"Pending", "Done"}


# --------- Validators ---------
def validate_description(desc: str):
    if not desc or not desc.strip():
        raise ValueError("Task description cannot be empty")


def validate_priority(priority: str):
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Priority must be one of {VALID_PRIORITIES}")


def validate_status(status: str):
    if status not in VALID_STATUSES:
        raise ValueError(f"Status must be one of {VALID_STATUSES}")


# --------- ObjectId helper ---------
def parse_object_id(id_str: str) -> ObjectId:
    """
    Accept a full 24‑hex ObjectId *or* a unique suffix (≥4 chars).
    Returns the matching ObjectId or raises ValueError.
    """
    id_str = id_str.strip()
    # Full 24‑char hex?
    if len(id_str) == 24:
        try:
            return ObjectId(id_str)
        except Exception:
            raise ValueError("Invalid full ObjectId format")

    # Otherwise treat as suffix
    if len(id_str) < 4:
        raise ValueError("ID suffix must be at least 4 characters")

    matches = [
        doc["_id"]
        for doc in tasks_collection.find({}, {"_id": 1})
        if str(doc["_id"]).endswith(id_str)
    ]
    if not matches:
        raise ValueError("Task not found for that ID")
    if len(matches) > 1:
        raise ValueError("ID suffix is ambiguous; use more characters")
    return matches[0]


# --------- Table formatter ---------
def format_tasks(task_docs):
    """
    Accepts an iterable of task documents and returns a Markdown‑style table
    (string) ready to print in the terminal.
    """
    rows = []
    for t in task_docs:
        # Show only last 6 chars of _id for brevity
        rows.append([
            str(t["_id"])[-6:],
            t["task"],
            t["priority"],
            t["status"],
            t["created_at"].strftime("%Y‑%m‑%d"),
        ])

    return tabulate(
        rows,
        headers=["ID", "Task", "Priority", "Status", "Created"],
        tablefmt="github"  # nice Markdown‑like style
    )

from datetime import datetime

def get_current_time():
    return datetime.now()
