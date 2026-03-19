from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass",
        database="testdb"
    )

@app.get("/items")
def read_items():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

@app.post("/items")
def create_item(name: str, description: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO items (name, description) VALUES (%s, %s)",
        (name, description)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"status": "created"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE items SET name=%s, description=%s WHERE id=%s",
        (name, description, item_id)
    )
    db.commit()
    cursor.close()
    db.close()
    return {"status": "updated"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM items WHERE id=%s", (item_id,))
    db.commit()
    cursor.close()
    db.close()
    return {"status": "deleted"}

