# Define structure of database in database models
from app import db
import sys
import os

class User(db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	complete_categories = db.Column(db.String(120), unique=False, nullable=False)
	complete_lessons = db.Column(db.String(120), unique=False, nullable=False)
	pos_statistics = db.relationship('POSStatistic', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Category(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    lessons = db.relationship('Lesson', backref='category', lazy=True)

class Lesson(db.model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=False, nullable=False)
    parts_of_speech = db.relationship('PartOfSpeech', backref='lesson', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class PartOfSpeech(db.model):
	id = db.Column(db.Integer, primary_key=True)
	l1 = db.Column(db.String(64), nullable=False)
	l2 = db.Column(db.String(64), nullable=False)
	lexical = db.Column(db.String(64), nullable=False)
	audio = db.Column(db.String(240), nullable=True)
	image = db.Column(db.String(240), nullable=True)
	lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)

class UserStatistic(db.model):
	id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
    	#return '<PartOfSpeech {} , {}>'.format(self.l2, self.lexical)

class POSStatistic(db.model):
	id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	last accessed = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
	num_accessed = db.Column(db.Integer, unique=False, nullable=False)
	num_incorrect = db.Column(db.Integer, unique=False, nullable=False)
	#difficulty
	pos_id = db.Column(db.Integer, db.ForeignKey('partofspeech.id'), unique=True, nullable=False)

    def __repr__(self):
    	return '<PartOfSpeech {} , {}>'.format(self.l2, self.lexical)

#class Challenge:
	# ID, category ID, type, question, answer, challenge (multiple choice, mixed words)
	# Access required fields from database to display
	# Store results to stats table