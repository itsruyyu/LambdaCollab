import json
import boto3
from decimal import Decimal
import uuid

# Inisialisasi klien DynamoDB
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('table-lambda')  # Pastikan tabel ini ada di DynamoDB

def lambda_handler(event, context):
    print(event)
    body = {}
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Menangani POST /todos untuk menambahkan todo baru
        if event['routeKey'] == "POST /todos":
            requestJSON = json.loads(event['body'])
            if not requestJSON.get('task'):
                statusCode = 400
                body = {'error': 'Task is required'}
            else:
                todo_id = str(uuid.uuid4())
                table.put_item(
                    Item={
                        'id': todo_id,
                        'task': requestJSON['task'],
                        'status': "pending"
                    }
                )
                body = {
                    'id': todo_id,
                    'task': requestJSON['task'],
                    'status': "pending"
                }

        # Menangani GET /todos untuk mendapatkan semua todos
        elif event['routeKey'] == "GET /todos":
            response = table.scan()
            todos = response.get("Items", [])
            body = todos

        # Menangani GET /todos/{id} untuk mendapatkan todo berdasarkan ID
        elif event['routeKey'] == "GET /todos/{id}":
            todo_id = event['pathParameters']['id'].strip()  # Menghapus karakter newline jika ada
            response = table.get_item(Key={'id': todo_id})
            if 'Item' not in response:
                statusCode = 404
                body = {'error': 'Todo not found'}
            else:
                body = response['Item']

        # Menangani PUT /todos/{id} untuk memperbarui todo berdasarkan ID
        elif event['routeKey'] == "PUT /todos/{id}":
            todo_id = event['pathParameters']['id'].strip()  # Menghapus karakter newline jika ada
            requestJSON = json.loads(event['body'])
            update_expression = "SET task = :task, #s = :status"
            expression_values = {
                ':task': requestJSON.get('task', 'No Task'),
                ':status': requestJSON.get('status', 'pending')
            }
            expression_attribute_names = {
                '#s': 'status'  # Alias untuk status
            }
            table.update_item(
                Key={'id': todo_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_values,
                ExpressionAttributeNames=expression_attribute_names
            )
            body = {'message': 'Updated todo ' + todo_id}

        # Menangani DELETE /todos/{id} untuk menghapus todo berdasarkan ID
        elif event['routeKey'] == "DELETE /todos/{id}":
            todo_id = event['pathParameters']['id'].strip()  # Menghapus karakter newline jika ada
            table.delete_item(Key={'id': todo_id})
            body = {'message': 'Deleted todo ' + todo_id}

        else:
            statusCode = 400
            body = {'error': 'Unsupported route: ' + event['routeKey']}
    
    except KeyError:
        statusCode = 400
        body = {'error': 'Invalid input'}
    except Exception as e:
        statusCode = 500
        body = {'error': str(e)}

    body = json.dumps(body)
    return {
        "statusCode": statusCode,
        "headers": headers,
        "body": body
    }
