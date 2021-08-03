from flask import Flask, request, jsonify

app = Flask(_name_)

user = [
    {"id": 1, "name": "john_doe_17091999"},
]


@app.get("/user")
def get_user():
    return jsonify(user)

@app.post("/user")
def add_user():
    if request.is_json:
        user = request.get_json()
        user.append(user)
        return user, 201
    return {"error": "Request must be JSON"}, 415
