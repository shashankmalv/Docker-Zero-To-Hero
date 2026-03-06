from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "db")
cache_host = os.getenv("CACHE_HOST", "redis")

def get_db_connection():
    conn = psycopg2.connect(
        host=db_host,
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

cache = redis.Redis(host=cache_host, port=6379)

@app.route("/")
def hello():

    visits = cache.incr("counter")

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        conn.close()
    except Exception as e:
        db_version = "Database connection failed"

    return f"""
    Hello from Flask DevOps App 🚀 <br>
    Redis Visits Counter: {visits} <br>
    PostgreSQL Version: {db_version}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)