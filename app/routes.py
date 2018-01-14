from flask import render_template
from app import app
import app.logic.course as course

@app.route('/')
def index():
	categories = Category.query.get(name)
	return render_template('index.html', title='Ewe Language Learning App',)

#def login():
	# reset challenge_tracker to 1
	# LoginForm
	# render: form

#def register():
	# reset challenge_tracker to 1
	# RegistrationForm
	# render: form

#def edit_profile():
	# reset challenge_tracker to 1
	# EditProfileForm
	# render: form

#def category():
	# reset challenge_tracker to 1
	# render: category name, lessons

@app.route('challenge/<category>')
def challenge():
	# ChallengeForm
	# render: question, form, keyboard
	# if correct: mark done, button reads next
	# if incorrect: button reads next