import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="soldiers_db"
    )


def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE intel_messages")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # each row is (Field, Type, Null, Key, Default, Extra)
    return [{"column": row[0], "type": row[1]} for row in rows] 

def get_all_messages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM intel_messages")
    all_msg = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_msg


def get_message_by_id(msg_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM intel_messages WHERE id = %s", (msg_id,))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data

def create_message(unit: str, classification: str, content: str, source:str | None) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO intel_messages (unit, classification, content, source) VALUES (%s, %s, %s, %s)"
    values = (unit, classification, content, source)

    cursor.execute(sql, values)
    conn.commit()

    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id


def update_messages(message_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    parts = [f"{k} = %s" for k in data.keys()]
    clause = ", ".join(parts)

    sql = f"UPDATE intel_messages SET {clause} WHERE id = %s"
    values = list(data.values()) + [message_id]

    cursor.execute(sql, values)
    conn.commit()

    change = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return change
    

def delete_message(msg_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM intel_messages WHERE id = %s", (msg_id,))
    conn.commit()

    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return deleted


