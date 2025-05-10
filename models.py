import sqlite3

def init_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute('''
        create table if not exists students(
            id INTEGER primary key autoincrement,
            name TEXT not null
        )
    ''')

    c.execute('''
        create table if not exists grades(
            id INTEGER primary key autoincrement,
            student_id INTEGER,
            subject TEXT,
            grade REAL
        )
    ''')

    c.execute("insert into students (name) values ('Pedro Infante')")
    c.execute("insert into students (name) values ('Sonia Miles')")

    c.execute("insert into grades (student_id, subject, grade) values (1, 'Matematicas', 4.5)")
    c.execute("insert into grades (student_id, subject, grade) values (1, 'Historia', 3.8)")
    c.execute("insert into grades (student_id, subject, grade) values (2, 'Matematicas', 4.5)")

    conn.commit()
    conn.close()
