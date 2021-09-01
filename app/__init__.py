from loader import save_subjects
from flask import abort, Flask, render_template
from sqlalchemy.exc import IntegrityError, InternalError, DataError

from app.models import Assessment, School_class, School_subject, Student
from app.db import db_session

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Classes'
        classes = db_session.query(School_class)
        db_session.close()
        return render_template('index.html', page_title=title, classes = classes)

    @app.route('/students/<int:class_id>')
    def students(class_id):
        title = 'Students'
        try:
            students = db_session.query(Student).filter(Student.school_class_id == class_id).all()
            
        except (IntegrityError, InternalError, DataError):
            db_session.close()
            abort(404)
        return render_template(
            'students.html',
            page_title=title,
            students=students
        )

    @app.route('/assessments/<int:student_id>')
    def assessments(student_id):
        title = 'Assessment'
        try:
            subjects = db_session.query(School_subject)
            assessments = db_session.query(Assessment).filter(Assessment.student_id == student_id)
        except (InternalError, IntegrityError, DataError):
            db_session.close()
            abort(404)
        return render_template(
            'assessment.html',
            page_title=title,
            assessments=assessments,
            subjects=subjects
        )

    return app