from flask import Flask, request, jsonify
from db_connection import get_db_connection
import json, os

app = Flask(__name__)

@app.route('/metrics', methods=['GET', 'POST'])
def metrics():
    if request.method == 'POST':
        data = request.get_json()
        
        # Store in database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO metrics (timestamp, hostname, cpu, ram, disk)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['time'], data['hostname'], data['cpu'], data['ram'], data['disk']))
        conn.commit()
        conn.close()
        
        return "Metrics received and stored", 200
    else:
        # Get from database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM metrics ORDER BY timestamp DESC")
        rows = cursor.fetchall()
        conn.close()
        
        metrics = []
        for row in rows:
            metrics.append({
                "time": row[0],
                "hostname": row[1], 
                "cpu": row[2],
                "ram": row[3],
                "disk": row[4]
            })
        return jsonify(metrics), 200

if __name__ == '__main__':
app.run(host="0.0.0.0", port=8000, debug=True)