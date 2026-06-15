import mysql.connector

conn = None

def get_connection():
    global conn
    if conn is None or not conn.is_connected():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database="students_db"
            )
            print("Database connection established successfully.")
        except Exception as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    return conn

def create_table():
    conn = get_connection()

    sql = """
    CREATE TABLE IF NOT EXISTS students(
        id INT PRIMARY KEY AUTO INCREMENT,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        course VARCHAR(100) NOT NULL,
        status VARCHAR(20) DEFAULT 'active',
        email VARCHAR(150) UNIQUE
        )
    """
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()
    return
