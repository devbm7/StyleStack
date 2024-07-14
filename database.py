import sqlite3
import pandas as pd
from PIL import Image
import io

def init_db():
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clothes
                      (id INTEGER PRIMARY KEY, category TEXT, image BLOB, name TEXT, status TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS laundry_history
                      (id INTEGER PRIMARY KEY, name TEXT, action TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def verify_user(username, password=None):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    if password:
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    else:
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_cloth_db(category, image, name):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clothes (category, image, name, status) VALUES (?, ?, ?, ?)', (category, img_byte_arr, name, 'In Closet'))
    conn.commit()
    conn.close()

def update_cloth_db(old_name, new_name, new_category, new_image):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    if new_image:
        img_byte_arr = io.BytesIO()
        new_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        cursor.execute('UPDATE clothes SET name = ?, category = ?, image = ? WHERE name = ?', (new_name, new_category, img_byte_arr, old_name))
    else:
        cursor.execute('UPDATE clothes SET name = ?, category = ? WHERE name = ?', (new_name, new_category, old_name))
    conn.commit()
    conn.close()

def delete_cloth_db(name):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clothes WHERE name = ?', (name,))
    conn.commit()
    conn.close()

def get_clothes_by_category_db(category=None):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    if category:
        cursor.execute('SELECT * FROM clothes WHERE category = ?', (category,))
    else:
        cursor.execute('SELECT * FROM clothes')
    clothes = cursor.fetchall()
    clothes_df = pd.DataFrame(clothes, columns=['id', 'category', 'image', 'name', 'status'])
    conn.close()
    return clothes_df

def get_clothes_by_status(status):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clothes WHERE status = ?', (status,))
    clothes = cursor.fetchall()
    clothes_df = pd.DataFrame(clothes, columns=['id', 'category', 'image', 'name', 'status'])
    conn.close()
    return clothes_df

def update_cloth_status(name, status):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE clothes SET status = ? WHERE name = ?', (status, name))
    conn.commit()
    conn.close()

def add_laundry_history(name, action):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO laundry_history (name, action) VALUES (?, ?)', (name, action))
    conn.commit()
    conn.close()

def get_laundry_history(name):
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM laundry_history WHERE name = ?', (name,))
    history = cursor.fetchall()
    history_df = pd.DataFrame(history, columns=['id', 'name', 'action', 'timestamp'])
    conn.close()
    return history_df

def get_laundry_due():
    conn = sqlite3.connect('clothes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, MAX(timestamp) as last_action_time FROM laundry_history WHERE action = "Sent to Laundry" GROUP BY name')
    due_clothes = cursor.fetchall()
    due_df = pd.DataFrame(due_clothes, columns=['name', 'last_action_time'])
    conn.close()
    return due_df
