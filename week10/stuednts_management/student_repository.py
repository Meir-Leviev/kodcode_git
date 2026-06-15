from db import get_connection

def add_student(data: dict):

    keys = ", ".join(data.keys())
    place_holders = (", ".join(["%s"] * len(data)))
    values = data.values()
    sql = f"""
        INSERT INTO students ({keys})
        VALUES ({place_holders})
    """
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        conn.commit()
        change = cursor.rowcount > 0
    return change


def get_all_students():
    sql = """
        SELECT * FROM students
    """
    conn = get_connection()
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        students = cursor.fetchall()
    return students


def get_student(id: int):
    sql = """
        SELECT * FROM students WHERE id = %s
    """
    conn = get_connection()
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql, (id,))
        students = cursor.fetchone()
    return students


def update_student(id, name: str):
    sql = "UPDATE students SET name = %s WHERE id = %s"
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql, (name, id))
        conn.commit()
        change = cursor.rowcount > 0
    return change



def delete_student(id):
    sql = "DELETE FROM students WHERE id = %s"
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql, (id,))
        conn.commit()
        change = cursor.rowcount > 0
    return change


def count_student():
    sql = "SELECT COUNT(*) AS count FROM students"
    conn = get_connection()
    with conn.cursor(dictionary=True) as cursor:
        cursor.execute(sql)
        result = cursor.fetchone()
    return result["count"]