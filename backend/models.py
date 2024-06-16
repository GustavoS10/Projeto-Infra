# backend/models.py
import psycopg2
import os

DATABASE_URL = os.getenv('DATABASE_URL')

def create_table():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            funcao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(nome, email, funcao):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, funcao) VALUES (%s, %s, %s)', (nome, email, funcao))
    conn.commit()
    conn.close()

def get_users():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    conn.close()
    return users

# Create the table if it doesn't exist
create_table()
