# backend/app.py
from flask import Flask, request, jsonify
from models import add_user, get_users

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def add_user_route():
    data = request.json
    add_user(data['nome'], data['email'], data['funcao'])
    return jsonify({'message': 'User added successfully!'}), 201

@app.route('/users', methods=['GET'])
def get_users_route():
    users = get_users()
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
