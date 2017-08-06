from model import User,Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


	need_to_know = session.query(Post).all

for thing in need_to_know:
	print(thing)