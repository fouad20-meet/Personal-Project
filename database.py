from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///people.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_person(name,email,phone,picture):
	person_object = Person(
		name = name,
		email=email,
		phone=phone,
		picture=picture)
	session.add(person_object)
	session.commit()

def query_by_id(person_id):
    person = session.query(Person).filter_by(id=person_id).first()
    return person_id

def delete_by_id(person_id):
	session.query(Person).filter_by(id=person_id).delete()
	session.commit()

def query_all():
	people = session.query(Person).all()
	return people

def delete_by_id(person_id):
	session.query(Person).filter_by(person_id=person_id).delete()
	session.commit()

