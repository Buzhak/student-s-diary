from posixpath import realpath
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db import Base, engine


class School_class(Base):
    __tablename__ = 'school_classes'

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    students = relationship('Student', back_populates='school_class', lazy='joined')

    def __repr__(self):
        return f'Class name: {self.name}'


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    school_class_id = Column(Integer, ForeignKey('school_classes.id'))
    school_class = relationship('School_class', back_populates='students')
    assessment = relationship('Assessment')

    def __repr__(self):
        return f'Student name: {self.name}'


class Assessment(Base):
    __tablename__ = 'assessment'

    id = Column(Integer, primary_key=True)
    assessment = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.id'))
    school_subject_id = Column(Integer, ForeignKey('school_subject.id'))
    school_subject = relationship('School_subject', lazy='joined')
   
    def __repr__(self):
        return self.assessment


class School_subject(Base):
    __tablename__ = 'school_subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    
    def __repr__(self):
        return f'{self.name}'

if __name__ == ('__main__'):
    Base.metadata.create_all(bind=engine)