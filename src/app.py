from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [] 

@app.route('/todos', methods=['POST'])
def add_todo():
    """
    Endpoint untuk menambahkan to-do baru..
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
    Endpoint untuk memperbarui to-do berdasarkan ID.
    """
    if todo_id >= len(todos):
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    todos[todo_id].update(data)
    return jsonify(todos[todo_id]), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    """
    Endpoint untuk mendapatkan semua to-do.
    """
    return jsonify(todos), 200

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """
    Endpoint untuk menghapus todo berdasarkan ID.
    """
    if todo_id >= len(todos):
        return jsonify({"error": "Todo not found"}), 404

    removed_todo = todos.pop(todo_id)
    return jsonify(removed_todo), 200

def lambda_handler(event, context):
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.serving import run_simple

    application = DispatcherMiddleware(app)

    return run_simple('0.0.0.0', 5000, application)

