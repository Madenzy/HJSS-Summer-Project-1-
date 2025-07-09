#create route to serve the index.html file
from flask import Flask, render_template

app = Flask(__name__)   
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/time-table')
def time_table():
    return render_template('timetable.html')


@app.route('/timetable-couch')
def time_table_couch():
    return render_template('timetable-couch.html')

@app.route('/timetable-grade')
def time_table_grade():
    return render_template('timetable-grade.html')


if __name__ == '__main__':
    app.run(debug=True)