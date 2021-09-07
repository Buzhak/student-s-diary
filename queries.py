from os import name
from app.db import db_session
from app.models import School_class, School_subject, Student, Assessment

def students_by_classes(class_name):
    class_ = School_class.query.filter(School_class.name == class_name).first()
    students = []
    if class_:
        for student in class_.students:
            students.append(f'{class_.name} - {student.name}')
    return students
    # query = db_session.query(School_class, Student).join(
    #     School_class, Student.school_class_id == School_class.id
    # ).filter(School_class.name == class_name)
    # student_s_list = []
    # for class_, student in query:
    #     student_s_list.append(f'{class_.name} - {student.name}')
    # return student_s_list

def assessment_by_student_and_subject(name, subject):
    result = db_session.query(Student, School_subject, Assessment).filter(
                              Assessment.school_subject_id == School_subject.id , Assessment.student_id == Student.id).filter(
                              Student.name == name, School_subject.name == subject).join(
                              Student, School_subject)
    assessment_list = []
    for student_name, school_subject, assessment in result:
        assessment_list.append(f'{student_name.name} - {school_subject.name} - {assessment.assessment}')

    return assessment_list   



if __name__ == ('__main__'):
    assessment_list = assessment_by_student_and_subject('Гедеон Изотович Бобылев', 'Математика')
    for row in assessment_list:
        print(row)