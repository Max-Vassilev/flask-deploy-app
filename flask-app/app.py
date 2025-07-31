from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_cars():
    conn = psycopg2.connect(
        host="your-rds-endpoint",
        database="yourdbname",
        user="youruser",
        password="yourpassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT brand, model FROM cars ORDER BY brand;")
    cars = cur.fetchall()
    cur.close()
    conn.close()
    return cars

@app.route('/')
def index():
    cars = get_cars()
    return render_template('index.html', cars=cars)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
