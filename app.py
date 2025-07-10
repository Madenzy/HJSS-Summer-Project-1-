from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/timetable', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.getlist('photos')
        for file in files:
            if file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('upload_file'))

    # List uploaded images
    images = os.listdir(UPLOAD_FOLDER)
    return render_template('timetable.html', images=images)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginchoice', methods=['GET', 'POST'])
def login_choice():
    if request.method == 'POST':
        user_type = request.form.get('user_type')
        return redirect(url_for('login', user_type=user_type))
    return render_template('loginchoice.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    user_type = request.args.get('user_type', 'user')  # default to 'user'
    if user_type == 'student':
        title = "Student Login"
    elif user_type == 'coach':
        title = "Coach Login"
    else:
        title = "User Login"
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return render_template('timetable.html', username=username)
    return render_template('login.html', title=title)

@app.route('/register')
def register():
    return render_template('register.html')
'''
@app.route('/timetable', methods=['GET', 'POST'])
def timetable():
    if request.method == 'POST':
        files = request.files.getlist('photos')
        for file in files:
            if file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('timetable'))

    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('timetable.html', images=images)'''

@app.route('/timetable-couch')
def time_table_couch():
    return render_template('timetable-couch.html')

@app.route('/timetable-grade')
def time_table_grade():
    return render_template('timetable-grade.html')

if __name__ == '__main__':
    app.run(debug=True)
