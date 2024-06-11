# backend/models.py
import sqlite3
import os

DATABASE_PATH = '/var/lib/sqlite3/database.db'

def create_table():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            funcao TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(nome, email, funcao):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, funcao) VALUES (?, ?, ?)', (nome, email, funcao))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    users = cursor.fetchall()
    conn.close()
    return users

# Create the table if it doesn't exist
create_table()
