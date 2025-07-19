import mysql.connector

def connect_and_fetch():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=33061,
            user='root',
            password='123456',
            database='test_db'
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        print("Tables in database:")
        for tbl in tables:
            print(f"- {tbl[0]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    connect_and_fetch()

