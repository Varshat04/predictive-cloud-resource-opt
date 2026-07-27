from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import joblib
import os

app = Flask(__name__)
CORS(app) 

# ==========================================
# 1. DATABASE INITIALIZATION
# ==========================================
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            full_name TEXT,
            password TEXT,
            role TEXT
        )
    ''')
    # Default Root Admin
    cursor.execute("INSERT OR IGNORE INTO users (user_id, full_name, password, role) VALUES ('admin_01', 'Akbar Naeem', 'admin123', 'ADMIN')")
    conn.commit()
    conn.close()

init_db()

# ==========================================
# 2. LOGIN API ENDPOINT
# ==========================================
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Check if user exists with matching password
    cursor.execute("SELECT full_name, role FROM users WHERE user_id=? AND password=?", (data['user_id'], data['password']))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"status": "success", "name": user[0], "role": user[1]})
    else:
        return jsonify({"status": "error", "message": "Invalid Identity or Security Key"}), 401

# ==========================================
# 3. REGISTER API ENDPOINT
# ==========================================
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO users (user_id, full_name, password, role) VALUES (?, ?, ?, ?)", 
                       (data['user_id'], data['name'], data['password'], data['role']))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Identity Created Successfully!"})
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"status": "error", "message": "User ID already exists in system!"}), 400

# ==========================================
# 4. REPORT METRICS API 
# ==========================================
@app.route('/api/reports', methods=['GET'])
def get_reports():
    try:
        metrics = joblib.load('report_metrics.pkl')
        return jsonify(metrics)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)