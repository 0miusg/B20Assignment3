import sqlite3
import os
from flask import Flask, render_template, request, g

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "assignment3.db")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def root():
    db = get_db()
    db.row_factory = make_dicts
    #check accout existance
    
    #if user not in Users, redirect to login page

    #if user in User,check whether student or instructor
        #if student redirect to student page
        #if instructor redirect to instructor page

    students=[]
    for student in query_db('select * from Students'):
        students.append(student)
    db.close()
    return render_template('instructor.html', student=students)

if __name__ == "__main__":
    app.run(debug=True)