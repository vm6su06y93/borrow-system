import os
from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
app.secret_key = 'abc123xyz'  # 可自訂

def get_db_connection():
    return psycopg2.connect(
        dbname='neondb',
        user='neondb_owner',
        password=os.environ.get('DB_PASSWORD'),
        host='ep-frosty-field-a139p6p3-pooler.ap-southeast-1.aws.neon.tech',
        sslmode='require'
    )

@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM devices ORDER BY id")
    devices = cur.fetchall()
    conn.close()
    return render_template("index.html", devices=devices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
