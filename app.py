from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/")
def home():
    return "Flask CI/CD ToDo API"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    task = data.get("task")
    tasks.append(task)
    return jsonify({"message": "Task added", "task": task})

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if index < len(tasks):
        removed = tasks.pop(index)
        return jsonify({"deleted": removed})
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)