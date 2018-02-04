S# Define structure of database in database models
from app import db, login
import sys
import os
from flask_login import UserMixin, login_manager

@login_manager.user_loader
def load_user(id):
    return User.get(int(id))

class User(UserMixin, db.model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	complete_categories = category_ids
	complete_lessons = lesson_ids

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Category(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    lessons = db.relationship('Lesson', backref='category', lazy=True)

class Lesson(db.model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=False, nullable=False)
    vocab = db.relationship('Vocabulary', backref='lesson', lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

class Vocabulary(db.model):
	id = db.Column(db.Integer, primary_key=True)
	l1 = db.Column(db.String(64), nullable=False)
	l2 = db.Column(db.String(64), nullable=False)
	lexical = db.Column(db.String(64), nullable=False)
	grammar = db.Column(db.String(64), nullable=False)
	audio = db.Column(db.String(240), nullable=True)
	image = db.Column(db.String(240), nullable=True)
	lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)

class Sentence(db.model):
	id = db.Column(db.Integer, primary_key=True)
	l1 = db.Column(db.String(64), nullable=False)
	l2 = db.Column(db.String(64), nullable=False)
	grammars = db.Column(db.String(64), nullable=False)
	audio = db.Column(db.String(240), nullable=True)
	image = db.Column(db.String(240), nullable=True)
	vocab_ids = db.relationship()

# Association
class UserCategory(db.model):
    user_id
    lesson_id
    available
    completed

# Association
class UserLesson(db.model):
    user_id
    lesson_id
    available
    completed

# Association
class UserVocabulary(db.model):
	user_id
	vocab_id
	introduced
	difficulty
	last accessed = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
	num_accessed = db.Column(db.Integer, unique=False, nullable=False)
	num_incorrect = db.Column(db.Integer, unique=False, nullable=False)

# Association
class UserSentence(db.model):
	user_id
	sentence_id
	available
	introduced
	last accessed
	num_accessed
	num_incorrect

#class Challenge:
	# ID, category ID, type, question, answer, challenge (multiple choice, mixed words)
	# Access required fields from database to display
	# Store results to stats table