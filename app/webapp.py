from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)  # Don't override template_folder

def get_tables():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=33061,
        user="root",
        password="123456",
        database="test_db"
    )
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    return [t[0] for t in tables]

@app.route("/")
def index():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=33061,
        user="root",
        password="123456",
        database="test_db"
    )
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES;")
    table_names = [row[0] for row in cursor.fetchall()]

    tables = []
    for name in table_names:
        cursor.execute(f"SELECT * FROM `{name}`")
        rows = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        tables.append({
            "name": name,
            "columns": columns,
            "rows": rows
        })

    cursor.close()
    conn.close()
    return render_template("index.html", tables=tables)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
