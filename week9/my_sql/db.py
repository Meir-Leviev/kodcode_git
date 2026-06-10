import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="soldiers_db",
    )


def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # each row is (Field, Type, Null, Key, Default, Extra)
    return [{"column": row[0], "type": row[1]} for row in rows]  # type: ignore


# INSERT logic
def create(name: str, rank: str, unit: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO soldiers (name, `rank`, unit) VALUES (%s, %s, %s)"
    values = (name, rank, unit)

    cursor.execute(sql, values)
    conn.commit()

    new_id = cursor.lastrowid

    cursor.close()
    conn.close()
    return new_id


# UPDATE logic
def update(soldier_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    set_parts = [f"`{key}` = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)

    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [soldier_id]

    cursor.execute(sql, values)
    conn.commit()

    changed = cursor.rowcount > 0

    cursor.close()
    conn.close()
    return changed


# DELETE logic
def delete(soldier_id: int) -> bool:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM soldiers WHERE id = %s", (soldier_id,))
    conn.commit()

    deleted = cursor.rowcount > 0

    cursor.close()
    conn.close()
    return deleted


def get_all() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # returns dicts instead of tuples

    cursor.execute("SELECT * FROM soldiers ORDER BY id ASC")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_by_id(soldier_id: int) -> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (soldier_id,))

    row = cursor.fetchone()  # returns one dict or None
    cursor.close()
    conn.close()
    return row


def get_name_and_rank() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT name, `rank` FROM soldiers")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows

