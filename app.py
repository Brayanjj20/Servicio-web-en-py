from flask import Flask, jsonify
import sqlite3

from models import init_db

app = Flask(__name__)

init_db()

def get_db_connection():
    conn = sqlite3.connect("students.db")
    conn.row_factory =sqlite3.Row
    return conn
    

@app.route('/students', methods=['GET'])
def get_all_students():
        conn =  get_db_connection()
        students = conn.execute('select * from students').fetchall()
        conn.close()
        return jsonify([dict(s) for s in students]) 

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_grades(student_id):
        conn =  get_db_connection()
        student = conn.execute('select * from students where id = ?', (student_id,)).fetchone()
        if student is None:
            return jsonify({"error": 'Estudiante no encontrado'}),404
        grades = conn.execute('select subject, grade from grades where student_id = ?', (student_id,)).fetchall()
        conn.close()
        return jsonify({
            'id':student['id'],
            'name': student['name'],
            'grades': [dict(g) for g in grades]
        })
        
@app.route('/grades', methods=['GET'])
def get_all_grades():
      conn = get_db_connection()
      grades =conn.execute('''
        select students.name, grades.subject,grades.grade from grades
            join students on grades.student_id = students.id        
                           ''').fetchall()
      conn.close()
      return jsonify([dict(g) for g in grades])

if __name__ == '__main__': 
      app.run(debug=True)


