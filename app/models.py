# Define structure of database in database models
from app import db, login
import sys
import os
from flask_login import UserMixin

#Association Tables:

vocab_grammar_assoc = db.Table('vocab_grammar_assoc', 
	db.Column('vocab_id', db.Integer, db.ForeignKey('vocab.id')), 
	db.Column('grammar_type', db.String(64), db.ForeignKey('grammar.name'))
)

vocab_english_assoc = db.Table('vocab_english_assoc', 
	db.Column('vocab_id', db.Integer, db.ForeignKey('vocab.id')), 
	db.Column('english_word', db.String(64), db.ForeignKey('english.word'))
)

@login.user_loader
def load_user(id):
	return User.get(int(id))

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	username = db.Column(db.String(64), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	#password_hash = db.Column(db.String(128))
	#vocab_accessed = relationship to UserVocabulary tble

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Category(db.Model):
	name = db.Column(db.String(64), nullable=False, primary_key=True)
	
	def __repr__ (self):
		return '<Category {}>'.format(self.name)

class Vocab(db.Model):
	id = db.Column(db.Integer, nullable=False, primary_key=True)
	ewe = db.Column(db.String(64), nullable=False)
	category = db.Column(db.String(64), db.ForeignKey('category.name'), nullable=False)
	audio = db.Column(db.String(240), nullable=True)
	image = db.Column(db.String(240), nullable=True)
	lexical = db.Column(db.String(240), nullable=True)
	grammar_types = db.relationship(
		'Grammar', 
		secondary=vocab_grammar_assoc,
		backref='ewe_vocabulary', 
		lazy='dynamic')
	english_words  = db.relationship(
		'English',
		secondary=vocab_english_assoc,
		backref='ewe_vocabulary', 
		lazy='dynamic')

	def __repr__ (self):
		return '<Vocab: Ewe: {},  {},  Lexical Class: {}, {} >'.format(self.ewe, self.english_words.all(), self.lexical, self.grammar_types.all())

class Lexical(db.Model):
	name = db.Column(db.String(64), nullable=False,  primary_key=True)

	def __repr__ (self):
		return '<Lexical Class: {}>'.format(self.name)

class Grammar(db.Model):
	name = db.Column(db.String(64), nullable=False, primary_key=True)

	def __repr__ (self):
		return '<Grammar Type: {}>'.format(self.name)

class English(db.Model):
	word = db.Column(db.String(64), nullable=False, primary_key=True)

	def __repr__ (self):
		return '<English: {}>'.format(self.word)

""""
# Association table
class UserVocabulary(db.Model):
	user_id
	ewe_vocab_id 
	introduced
	difficulty
	#last accessed = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
	num_accessed = db.Column(db.Integer, unique=False, nullable=False)
	num_incorrect = db.Column(db.Integer, unique=False, nullable=False)
"""

# Association

#class Challenge:
	# ID, category ID, type, question, answer, challenge (multiple choice, mixed words)
	# Access required fields from database to display
	# Store results to stats table