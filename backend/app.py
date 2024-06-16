from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.json
        name = data['name']
        email = data['email']
        role = data['role']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO usuarios (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'status': 'User added'}), 201

    if request.method == 'GET':
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT name, email, role FROM usuarios')
        users = cur.fetchall()
        cur.close()
        conn.close()

        users_list = [{'name': user[0], 'email': user[1], 'role': user[2]} for user in users]
        return jsonify(users_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
