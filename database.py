import sqlite3

def init_db():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            receiver TEXT,
            message TEXT,
            encrypted_message TEXT,
            otp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_message(sender, receiver, message, encrypted_message, otp):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (sender, receiver, message, encrypted_message, otp)
        VALUES (?, ?, ?, ?, ?)
    ''', (sender, receiver, message, encrypted_message, otp))
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return messages
