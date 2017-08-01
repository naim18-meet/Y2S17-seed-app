from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__  = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(first_name + " " + last_name)
    email = (String(100))
    password = (String(50))

class Post(Base):
	__tablename__  = 'post'
	id = Column(Integer, primary_key=True)
	user_id = relationship('User')
	title = Column(Text ?(50))
	content = Column(String(1000))
	video_url = Column(String(500))
	image_url = Column(String(500))
	category = Column(String(20))
    # ADD YOUR FIELD BELOW ID

# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel
