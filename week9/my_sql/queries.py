from db import get_connection


def get_by_rank(rank):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM soldiers WHERE `rank` = %s", (rank,))
    ret_val = cursor.fetchall()

    cursor.close()
    conn.close()
    return ret_val


def get_active_sorted(active=True, order="asc"):
    if order.lower() not in ("asc", "desc"):
        order = "asc"
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if active:
        sql = f"SELECT * FROM soldiers WHERE active = TRUE ORDER BY name {order.upper()}"
    else:
        sql = f"SELECT * FROM soldiers WHERE active = FALSE ORDER BY name {order.upper()}"
    
    cursor.execute(sql)
    ret_val = cursor.fetchall()

    cursor.close()
    conn.close()
    return ret_val



def get_distinct_units():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"SELECT DISTINCT unit FROM soldiers")
    units = cursor.fetchall()
    
    # to get a list of units
    units = [u['unit'] for u in units]
    cursor.close()
    conn.close()
    return units


def search_by_name(term):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    search_term = f"%{term}%"
    cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s", (search_term,))
    ret_val = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return ret_val


def get_missing_rank():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM soldiers WHERE `rank` IS NULL")
    ret_val = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return ret_val


def get_by_unit(unit):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM soldiers WHERE unit = %s ORDER BY name ASC", (unit,))
    ret_val = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return ret_val
