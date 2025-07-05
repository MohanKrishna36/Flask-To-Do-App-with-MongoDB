"""
main.py
CLI entry point for the Mongo‑powered To‑Do app.
"""

import sys

from db import ping
import utils
import task_operations as ops


MENU = """
===============================
1.  Create task
2.  View tasks
3.  Update task
4.  Delete task
5.  Exit
-------------------------------
"""


# ---------- Handler functions ----------
def prompt_choice() -> str:
    print(MENU)
    return input("Select an option ⟩ ").strip()


def handle_create():
    desc = input("Task description: ").strip()
    prio = input("Priority (High/Medium/Low) [Medium]: ").strip() or "Medium"
    try:
        _id = ops.create_task(desc, prio)
        print(f"✅  Created with ID {_id}")
    except Exception as e:
        print(f"❌  {e}")


def handle_view():
    tasks = ops.fetch_all_tasks()
    if tasks:
        print(utils.format_tasks(tasks))
    else:
        print("No tasks yet!\n")

'''
# in handle_view() temporarily:
for t in ops.fetch_all_tasks():
    print(t["_id"], t["task"])
'''


def handle_update():
    task_id = input("Enter task ID (full _id or last 6 chars): ").strip()
    print("Leave any field blank to keep it unchanged.")
    desc = input("New description: ")
    prio = input("New priority (High/Medium/Low): ").strip()
    stat = input("New status (Pending/Done): ").strip()

    # Convert blank → None
    desc = desc if desc.strip() else None
    prio = prio or None
    stat = stat or None

    try:
        ops.update_task(task_id, description=desc, priority=prio, status=stat)
        print("✅  Task updated")
    except Exception as e:
        print(f"❌  {e}")


def handle_delete():
    task_id = input("Enter task ID to delete: ").strip()
    try:
        ops.delete_task(task_id)
        print("✅  Task deleted")
    except Exception as e:
        print(f"❌  {e}")


# ---------- Main loop ----------
def main():
    # Quick DB connectivity check
    try:
        ping()
    except Exception as db_err:
        print(f"Cannot connect to MongoDB → {db_err}")
        sys.exit(1)

    handlers = {
        "1": handle_create,
        "2": handle_view,
        "3": handle_update,
        "4": handle_delete,
        "5": lambda: sys.exit(0),
    }

    while True:
        choice = prompt_choice()
        handler = handlers.get(choice)
        if handler:
            handler()
        else:
            print("⚠️  Invalid choice")


if __name__ == "__main__":
    main()
