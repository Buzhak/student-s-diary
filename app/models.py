from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db import Base, engine


class School_class(Base):
    __tablename__ = 'school_class'

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    students = relationship('Student', back_populates='school_class')


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primaty_key=True)
    name = Column(String(100))
    school_class_id = Column(Integer, ForeignKey('school_class.id'))
    school_class = relationship('School_class', back_populates='students')
    assessments = relationship('Assessment')


class Assessment(Base):
    __tablename__ = 'assessment'

    id = Column(Integer, primary_key=True)
    assessment = Column(Integer(1))
    student_id = Column(Integer, ForeignKey('student.id'))
    school_subject_id = Column(Integer, ForeignKey('school_subject.id'))
    school_subject = relationship('School_subject', back_populates='assessments')


class School_subject(Base):
    __tablename__ = 'school_subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    assessments = relationship('Assessment', back_populates='school_subject')

if __name__ == ('__main__'):
    Base.metadata.create_all(bind=engine)