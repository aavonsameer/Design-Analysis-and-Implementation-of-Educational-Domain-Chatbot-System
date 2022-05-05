import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()

class Accounts(Base):
    __tablename__ = 'accounts'
    id = Column(String, primary_key=True)
    name = Column(String(250),nullable=False)
    user_type = Column(String(250), nullable=False)
    password = Column(String(250))
class Departments(Base):
    __tablename__ = 'departments'
    did = Column(Integer, primary_key=True)
    name = Column(String(30),nullable=False)
class CSE_Subjects():
    sub_id = Column(Integer, primary_key=True)
    sub_name = Column(Integer)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    departments = relationship(Departments)
    year = Column(Integer)
    sem = Column(Integer)
class Students(Base):
    __tablename__ = 'students'
    sid = Column(String, primary_key=True)
    sname = Column(String(30),nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    departments = relationship(Departments)
class Faculty(Base):
    __tablename__ = 'faculty'
    id = Column(String, primary_key=True)
    name = Column(String(30),nullable=False)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    departments = relationship(Departments)
class Student_Profile(Base):
    __tablename__ = 'student_profile'
    sid = Column(String, primary_key=True)
    name = Column(String(30),nullable=False)
    branch = Column(String(30),nullable=False)
    year = Column(Integer)
    gender = Column(String(30),nullable=False)
    dob = Column(DateTime, nullable=True)
    entrance_type = Column(String(30))
    HorD = Column(String)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    departments = relationship(Departments)
    faculty_id = Column(String, ForeignKey('faculty.id'))
    faculty = relationship(Faculty)
class Faculty_Profile(Base):
    __tablename__ = 'faculty_profile'
    id = Column(String, primary_key=True)
    name = Column(String(30),nullable=False)
    branch = Column(String(30),nullable=False)
    gender = Column(String(30))
    dob = Column(DateTime)
    phone = Column(Integer)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    departments = relationship(Departments)
class Marks(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    student_id = Column(String(30),ForeignKey('student_profile.sid'))
    Student = Column(String(30))
    student_profile = relationship(Student_Profile) 
    s34 = Column(Integer)
    s32 = Column(Integer)
    s38 = Column(Integer)
    s40 = Column(Integer)
    s35 = Column(Integer)
    s26 = Column(Integer)
    s17 = Column(Integer)
    s38 = Column(Integer)
    s29 = Column(Integer)
    s30 = Column(Integer)
    t319 = Column(Integer)
    a32 = Column(Integer)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    departments = relationship(Departments)
    year = Column(Integer)
    faculty_id = Column(String, ForeignKey('faculty.id'))
    councelor_id = Column(String, ForeignKey('faculty.id'))
    faculty = relationship(Faculty)
    sem = Column(Integer)
class Subjects(Base):
    __tablename__ = 'subjects'
    code = Column(String, primary_key=True)
    name = Column(String)
    sem = Column(String)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    year = Column(Integer)
class Attendance(Base):
    __tablename__ = 'attendance'
    sid = Column(Integer, primary_key=True)
    #total_days = Column(Integer)
    student_id = Column(String, ForeignKey('student_profile.sid'))
    student_profile = relationship(Student_Profile) 
    student_name = Column(String)
    s89 = Column(Integer)
    s52 = Column(Integer)
    s63 = Column(Integer)
    s44 = Column(Integer)
    s95 = Column(Integer)
    s86 = Column(Integer)
    s97 = Column(Integer)
    s28 = Column(Integer)
    s39 = Column(Integer)
    s100 = Column(Integer)
    s61= Column(Integer)
    s82 = Column(Integer)
    s73 = Column(Integer)
    s94 = Column(Integer)
    attend=Column(Integer)
    attend_perc = Column(Integer)
    dept_id = Column(Integer, ForeignKey('departments.did'))
    year = Column(Integer)
    departments = relationship(Departments)
    faculty_id = Column(String, ForeignKey('faculty.id'))
    councelor_id = Column(String, ForeignKey('faculty.id'))
    faculty = relationship(Faculty)
    sem = Column(Integer)
    
class Faculty_Feedback(Base):
    __tablename__ = 'faculty_feedback'
    id = Column(Integer, primary_key=True)
    sub1 = Column(Integer)
    sub2 = Column(Integer)
    sub3 = Column(Integer)
    sub4 = Column(Integer)
    sub5 = Column(Integer)
    sub6 = Column(Integer)
    lab1 = Column(Integer)
    lab2 = Column(Integer)
    date = Column(DateTime)
    faculty_id = Column(String, ForeignKey('faculty.id'))
    faculty = relationship(Faculty)
    student_id = Column(String, ForeignKey('student_profile.sid'),unique=True)
    student_profile = relationship(Student_Profile) 
class Feedback(Base):
    __tablename__ = 'feedback'
    sid = Column(Integer, primary_key=True)
    name = Column(String(30))
    subject = Column(String(30),nullable=False)
    message = Column(String(300),nullable=False)
    user_id = Column(String(30), ForeignKey('accounts.id'))

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
