from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


# -------------------------------
# Database Model
# -------------------------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    emergency_contact = db.Column(db.String(15), unique=True, nullable=False)
    grade_level = db.Column(db.String(10), nullable=False)
    medical_notes = db.Column(db.Text, nullable=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()


# -------------------------------
# Routes
# -------------------------------
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loginchoice', methods=['GET', 'POST'])
def login_choice():
    return render_template('loginchoice.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Student Login"
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # TODO: verify student login here
        return render_template('timetable.html', username=username)
    return render_template('login.html', title=title)


@app.route('/coach-login', methods=['GET', 'POST'])
def coach_login():
    title = "Coach Login"
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('couch-timetable.html', username=username)
    return render_template('couch-login.html', title=title)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        age = request.form.get('age')
        gender = request.form.get('gender')
        emergency_contact = request.form.get('emergency_contact')
        grade_level = request.form.get('grade_level')
        medical_notes = request.form.get('medical_notes')
        username = request.form.get('username')
        password = request.form.get('password')

        new_student = Student(
            fullname=fullname,
            age=age,
            gender=gender,
            emergency_contact=emergency_contact,
            grade_level=grade_level,
            medical_notes=medical_notes,
            username=username,
            password=password
        )

        try:
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return f'An error occurred: {e}'

    return render_template('register.html')


@app.route('/timetable-coach')
def time_table_coach():
    return render_template('timetable-coach.html')


@app.route('/timetable-grade')
def time_table_grade():
    return render_template('timetable-grade.html')


@app.route('/students')
def get_students():
    students = Student.query.all()
    print("DEBUG:", students)  
    return render_template('students.html', students=students)

@app.route('/mee')
def mee():
    students = Student.query.all()
    return render_template('mee.html', students=students)
# -------------------------------
# Run App
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
