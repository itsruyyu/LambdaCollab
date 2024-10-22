import app

def test_post_task():
    event = {
        'httpMethod': 'POST',
        'path': '/tasks',
        'body': '{"task": "Learn Lambda"}'
    }
    response = app.lambda_handler(event, None)
    assert response['statusCode'] == 201

def test_put_task():
    app.tasks = [{'id': 1, 'task': 'Learn Lambda', 'completed': False}]
    event = {
        'httpMethod': 'PUT',
        'path': '/tasks/1',
        'pathParameters': {'task_id': '1'},
        'body': '{"task": "Learn Lambda Updated", "completed": true}'
    }
    response = app.lambda_handler(event, None)
    assert response['statusCode'] == 200

