from flask import Flask, render_template
import psycopg2
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    try:
        conn = psycopg2.connect(app.config['SQLALCHEMY_DATABASE_URI'])
        return conn
    except Exception as e:
        print(f"Unable to connect to the database: {e}")
        return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        message = "Successfully connected to the database."
        conn.close()
    else:
        message = "Failed to connect to the database."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
