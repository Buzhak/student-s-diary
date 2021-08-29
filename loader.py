import csv

from app.db import db_session
from app.models import School_class, Student, Assessment, School_subject

def read_csv(filename):
    with open(filename, "r", encoding='utf-8') as f:
        fields = ['school_class', 'student', 'assessment', 'subject']
        reader = csv.DictReader(f, fields, delimiter=';')
        data = []
        for row in reader:
            data.append(row)
        return data

def save_classes(data):
    processed = []
    unique_class = []
    for row in data:
        if row['school_class'] not in processed:
            school_class = {'name': row['school_class']}
            unique_class.append(school_class)
            processed.append(school_class['name'])
    db_session.bulk_insert_mappings(School_class, unique_class, return_defaults=True)
    db_session.commit()
    return unique_class

def get_class_id(classes, class_name):
    for class_ in classes:
        if class_['name'] == class_name:
            return class_['id']


def save_students(data, classes):
    processed = []
    unique_students = []
    for row in data:
        if row['student'] not in processed:
            student = {'name':row['student'], 'school_class_id': get_class_id(classes, row['school_class'])}
            unique_students.append(student)
            processed.append(student['name'])
    db_session.bulk_insert_mappings(Student, unique_students, return_defaults=True)
    db_session.commit()
    return unique_students

def save_subjects(data):
    processed = []
    unique_subjects = []
    for row in data:
        if row['subject'] not in processed:
            subject = {'name':row['subject']}
            unique_subjects.append(subject)
            processed.append(subject['name'])
    db_session.bulk_insert_mappings(School_subject, unique_subjects, return_defaults=True)
    db_session.commit()
    return unique_subjects

def get_student_id(students, student_name):
    for student in students:
        if student['name'] == student_name:
            return student['id']
        
def get_subject_id(subjects, subject_name):
    for subject in subjects:
        if subject['name'] == subject_name:
            return subject['id']
        

def save_assessments(data, students, subjects):
    assessments =[]
    for row in data:
        assessment = {'assessment':row['assessment'], 'student_id':get_student_id(students, row['student']), 'school_subject_id':get_subject_id(subjects, row['subject'])}
        assessments.append(assessment)
    db_session.bulk_insert_mappings(Assessment, assessments)
    db_session.commit()
        

if __name__ == ('__main__'):
    all_data = read_csv('students.csv')
    classes = save_classes(all_data)
    students = save_students(all_data, classes)
    subjects = save_subjects(all_data)
    assessments = save_assessments(all_data, students, subjects)
    print("the end")
