# flask-deploy-app
Simple Flask application which will be deployed on AWS

# Flask App with PostgreSQL

Simple app showing best cars from a local PostgreSQL database.

---

## Setup

Create table:

```sql
CREATE TABLE cars (
  id SERIAL PRIMARY KEY,
  brand VARCHAR(100),
  model VARCHAR(100)
);
```

Insert sample data:

```sql
INSERT INTO cars (brand, model) VALUES
('Porsche', '911'),
('Ferrari', 'Enzo'),
('Lamborghini', 'Aventador');
```
---

## Run

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser.
