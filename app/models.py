from posixpath import realpath
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db import Base, engine


class School_class(Base):
    __tablename__ = 'school_classes'

    id = Column(Integer, primary_key=True)
    name = Column(String(3))
    students = relationship('Student', back_populates='school_class')

    def __repr__(self):
        return f'Class name: {self.name}'


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    school_class_id = Column(Integer, ForeignKey('school_classes.id'))
    school_class = relationship('School_class', back_populates='students')

    def __repr__(self):
        return f'Student name: {self.name}'


class School_subject(Base):
    __tablename__ = 'school_subject'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    
    def __repr__(self):
        return f'School_subjec: {self.name}'


class Assessment(Base):
    __tablename__ = 'assessment'

    id = Column(Integer, primary_key=True)
    assessment = Column(Integer)
   
    def __repr__(self):
        return self.assessment

if __name__ == ('__main__'):
    Base.metadata.create_all(bind=engine)