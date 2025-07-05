from flask import Blueprint, render_template, request, redirect, url_for, flash
import task_operations as ops

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        priority = request.form.get("priority")
        status = request.form.get("status")

        if task:
            ops.create_task(task, priority, status)
            flash("Task created!", "success")
        else:
            flash("Task cannot be empty.", "danger")
        return redirect(url_for("main.index"))

    # GET request — show task list
    tasks = ops.fetch_all_tasks()
    return render_template("index.html", tasks=tasks)


from bson import ObjectId

@main.route("/delete/<task_id>", methods=["POST"])
def delete_task(task_id):
    try:
        ops.delete_task(ObjectId(task_id))
        flash("Task deleted.", "success")
    except Exception as e:
        flash(f"Error deleting task: {e}", "danger")
    return redirect(url_for("main.index"))



@main.route("/edit/<task_id>", methods=["GET"])
def edit_task_form(task_id):
    task = ops.get_task_by_id(task_id)
    if not task:
        flash("Task not found.", "danger")
        return redirect(url_for("main.index"))
    return render_template("edit.html", task=task)


@main.route("/update/<task_id>", methods=["POST"])
def update_task(task_id):
    task = ops.get_task_by_id(task_id)
    if not task:
        flash("Task not found.", "danger")
        return redirect(url_for("main.index"))

    description = request.form.get("task")
    priority = request.form.get("priority")
    status = request.form.get("status")

    try:
        ops.update_task(task_id, description, priority, status)
        flash("Task updated!", "success")
    except Exception as e:
        flash(f"Update failed: {e}", "danger")

    return redirect(url_for("main.index"))
