from flask import Blueprint, render_template
from datetime import datetime
import sqlite3, os

bp = Blueprint("main", __name__, url_prefix="/")

DB_FILE = os.environ.get("DB_FILE")

@bp.route("/")
def main():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, name, start_datetime, end_datetime, description, private
            FROM appointments
            ORDER BY start_datetime;
        """)
        rows = cursor.fetchall()


    appointments = []
    for row in rows:
        appointments.append({
            "id": row[0],
            "name": row[1],
            "start": datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S'),
            "end": datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S'),
            "description": row[4],
            "private": bool(row[5])
        })

    return render_template("main.html", appointments=appointments)
