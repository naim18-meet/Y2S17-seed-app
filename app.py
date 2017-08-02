# flask imports
from flask import Flask, Response, render_template, request, redirect, url_for

# flask setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "ITSASECRET"

# flask-login imports
from flask_login import login_required, current_user
from login import login_manager, login_handler, logout_handler
login_manager.init_app(app)

# SQLAlchemy

from model import Base,User,Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def hello_world():
    posts=session.query(Post).all()    
    return render_template('index.html' ,posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return login_handler(request)


@app.route('/logout')
def logout():
  return logout_handler()


@app.route('/protected', methods=["GET"])
@login_required
def protected():
    return render_template('protected.html')


@app.route('/Category/Clothes')
def Clothes():
	return render_template('lifehacxcat.html')

@app.route('/Category/Garden')
def Garden():
	return render_template('lifehacxcat.html')

@app.route('/Category/Kitchen')
def Kitchen():
	return render_template('lifehacxcat.html')

@app.route('/Category/Makeup')
def Makeup():
	return render_template(' .html')

@app.route('/Category/HomeDesign')
def Home_Design():
	return render_template('lifehacxcat.html')

@app.route('/Category/Camping')
def Camping():
	return render_template('lifehacxcat.html')

@app.route('/Category/Other')
def Other():
	return render_template('lifehacxcat.html')

@app.route('/Add_Hack', methods=["GET", "POST"])
def Add_Hack():
	if request.method == "GET":
		#show the webpage
		return render_template('Add_Hack.html')	
	if request.method == "POST":
		vid_url = request.form.get("vid_url")
		title = request.form.get("title")
		category = request.form.get("category")
		description = request.form.get("description")



		


		embed_video = vid_url
		
		vid_url = 'https://youtube.com/embed/'+ embed_video.split('=')[1]

		new_post = Post(title=title, description=description,
			video_url=vid_url,category=category)
		session.add(new_post)
		session.commit()
		return redirect(url_for('hello_world'))

		# redirect
@app.route('/', methods=["GET","POST"])
def Add_user():


	'''
	THINGS IN A POST

	title = Column(Text (50))
 	description = Column(String(1000))
 	video_url = Column(String(500))
 	category = Column(String(20))


 	BACKEND HTML

	title
	category
	vid_url
	description

 	'''