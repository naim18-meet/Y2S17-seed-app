from sqlalchemy import Column, DateTime, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__  = 'User'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(100))
    email = Column(String(100))
    password = Column(String(50))

class Post(Base):
	__tablename__  = 'Post'
	id = Column(Integer, primary_key=True)
	#user_id = relationship(User)
	title = Column(Text(50))
	content = Column(String(1000))
	video_url = Column(String(500))
	image_url = Column(String(500))
	category = Column(String(20))
    # ADD YOUR FIELD BELOW ID



# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel
