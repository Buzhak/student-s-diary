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

def assessment_by_student_and_subject(name, school_subject):
    result = db_session.query(Assessment).join(
        Assessment, Assessment.student_id == Student.id, Assessment.school_subject_id == School_subject.id
        ).filter(Student.name == name, School_subject.name == school_subject).all()
    assessment_list = []
    for row in result:
        assessment_list.append(f'{row.assessment}')

    return assessment_list   
# тут я все сломал!!!


if __name__ == ('__main__'):
    assessment_list = assessment_by_student_and_subject('Корнил Гертрудович Мишин', 'Русский')
    for row in assessment_list:
        print(row)