from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []  

@app.route('/todos', methods=['POST'])
def add_todo():
    """
    Endpoint untuk menambahkan todo baru.
    """
    data = request.get_json()
    if not data.get('task'):
        return jsonify({"error": "Task is required"}), 400

    todo = {
        "id": len(todos),
        "task": data['task'],
        "status": "pending"
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """
    Endpoint untuk memperbarui todo berdasarkan ID.
    """
    if todo_id >= len(todos):
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    todos[todo_id].update(data)
    return jsonify(todos[todo_id]), 200
