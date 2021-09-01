import csv
import random

from faker import Faker


fake = Faker('ru_RU')

def get_clsasses():
    return [['1А'], ['1Б'], ['1В'], ['1Г']]

def get_subjects():
    return [['Русский'], ['Математика'], ['Физкультура'], ['ИЗО']]

def get_fake_students(classes, num_students=25):
    students = []
    for class_ in classes:
        for _ in range(num_students):
            students.append(class_ + [fake.name()])

    return students

def get_assessments_by_subjects(students):
    assessments = []
    assessments_by_subjects = get_subjects()
    for student in students:
        for assessment in assessments_by_subjects:
            assessments.append(student + assessment)

    return assessments

def get_assessments(subjects, num_assessments=10):
    assessments_by_subjects = []
    for subject in subjects:
        for _ in range(num_assessments):
            assessments_by_subjects.append(subject + [random.randint(2,5)])

   
    return assessments_by_subjects

def generate_data(assessments):
    with open('students.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        for assessment in assessments:
            writer.writerow(assessment)
            


if __name__ == ('__main__'):
    classes = get_clsasses()
    students = get_fake_students(classes)
    subjects = get_assessments_by_subjects(students)
    assessments = get_assessments(subjects)

    
    generate_data(assessments)


    # generate_data()