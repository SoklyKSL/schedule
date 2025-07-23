import mysql.connector
from config import DB_CONFIG

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

def add_or_update_user(telegram_id, name, phone_number, role='user', position=None):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM users WHERE telegram_id = %s", (telegram_id,))
    if cursor.fetchone():
        conn.close()
        return False  # User already exists

    cursor.execute("""
        INSERT INTO users (name, phone_number, telegram_id, position, type)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, phone_number, telegram_id, position, role))

    conn.commit()
    cursor.close()
    conn.close()
    return True
