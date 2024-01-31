from flask import Flask, Blueprint, jsonify, request
from jsonschema import validate, ValidationError
from schemas import task_schema, tasks_schema, delete_tasks_schema

app = Flask(__name__)

tasks = [{"id": 1, "title": "example task", "is_completed": False}]
counter = 1


@app.route("/")
def welcome():
    return "<h3>Waterdip AI Assignment by Shubham Prasad</h3>"


v1 = Blueprint("v1", __name__, url_prefix="/v1")


# get all tasks and create a task
@v1.route("/tasks", methods=["GET", "POST", "DELETE"])
def create_task():
    global counter
    if request.method == "GET":
        return jsonify({"tasks": tasks}), 200

    elif request.method == "POST":
        if "tasks" in request.json:
            schema = tasks_schema
        else:
            schema = task_schema

        try:
            validate(request.json, schema)

            if "tasks" in request.json:
                for t in request.json["tasks"]:
                    task = {
                        "id": counter + 1,
                        "title": t.get("title"),
                        "is_completed": t.get("is_completed", False),
                    }
                    tasks.append(task)
                    counter += 1
                return "", 201
            else:
                task = {
                    "id": counter + 1,
                    "title": request.json.get("title"),
                    "is_completed": request.json.get("is_completed", False),
                }
                tasks.append(task)
                counter += 1
                return jsonify({"id": task["id"]}), 201
        except ValidationError:
            return jsonify({"error": "Invalid request"}), 400

    elif request.method == "DELETE":
        if "tasks" in request.json:
            try:
                validate(request.json, delete_tasks_schema)
                for t in request.json["tasks"]:
                    task_id = t["id"]
                    tasks[:] = [task for task in tasks if task["id"] != task_id]
                return "", 204
            except ValidationError:
                return jsonify({"error": "Invalid request"}), 400


# get a task by id, delete a task by id, edit a task by id
@v1.route("/tasks/<int:id>", methods=["GET", "DELETE", "PUT"])
def task_by_id(id: int):
    if request.method == "GET":
        for task in tasks:
            if task["id"] == id:
                return jsonify(task), 200
        return jsonify({"error": "There is no task at that id"}), 404
    elif request.method == "DELETE":
        tasks[:] = [task for task in tasks if task["id"] != id]
        return "", 204
    elif request.method == "PUT":
        task = next((t for t in tasks if t["id"] == id), None)
        if task:
            is_valid = False
            if "title" in request.json:
                task["title"] = request.json["title"]
                is_valid = True
            if "is_completed" in request.json:
                task["is_completed"] = request.json["is_completed"]
                is_valid = True
            if is_valid:
                return "", 204
            else:
                return jsonify({"error": "Invalid request"}), 400
        else:
            return jsonify({"error": "There is no task at that id"}), 404


app.register_blueprint(v1)
