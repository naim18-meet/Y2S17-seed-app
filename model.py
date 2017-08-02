

from flask_login import UserMixin

from sqlalchemy import Column, DateTime, Integer, String, Boolean, Text

from sqlalchemy.ext.declarative import declarative_base

from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()



class User(UserMixin, Base):
    __tablename__ = 'user'
    id            = Column(Integer, primary_key=True)
    email         = Column(String)
    pw_hash       = Column(String)
    authenticated = Column(Boolean, default=False)

    def __repr__(self):
      return "<User: %s, password: %s>" % (
        self.email, self.pw_hash)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

#     first_name = Column(String(50))
#     last_name = Column(String(50))
#     user_name = Column(first_name + " " + last_name)
#     email = (String(100))
#     password = (String(50))


class Post(Base):
 	__tablename__  = 'post'
 	id = Column(Integer, primary_key=True)
    #user_id = relationship('User')
 	title = Column(Text (50))
 	description = Column(String(1000))
 	video_url = Column(String(500))
 	category = Column(String(20))

 	def __repr__(self):
 		return self.title + " " + self.description + " " +self.video_url + " " + self.category
     # ADD YOUR FIELD BELOW ID




# IF YOU NEED TO CREATE OTHER TABLE 
# FOLLOW THE SAME STRUCTURE AS YourModel
