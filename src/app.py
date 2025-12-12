from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)



  

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     body = request.get_json()
#     if body is None:
#         return jsonify(
#             {
#                 "msg": "Invalid JSON body",
#             }
#         ), 400
#     if 'email' not in body:
#         return jsonify({ "msg": "Missing 'email' field" }), 400



#     print(body)
#     return jsonify(
#         {
#             "msg": "Todo added successfully",
#         }
#     ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 3245, debug=True)
