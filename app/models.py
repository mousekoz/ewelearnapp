# Define structure of database in database models
from app import db, login
import sys
import os
from flask_login import UserMixin

#Association Tables:

lexical_classes = db.Table('lexical_classes', db.Column('ewe_vocab_id', db.Integer, db.ForeignKey('ewevocabulary.id')), 
												db.Column('lexical_name', db.String(64), db.ForeignKey('lexicalclass.name')))

grammar_types = db.Table('grammar_types', db.Column('ewe_vocab_id', db.Integer, db.ForeignKey('ewevocabulary.id')), 
												db.Column('grammar_type', db.String(64), db.ForeignKey('grammartype.name')))

@login.user_loader
def load_user(id):
    return User.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
	#password_hash = db.Column(db.String(128))
	#vocab_accessed = relationship to UserVocabulary tble

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Category(db.Model):
    name = db.Column(db.String(64), primary_key=True)

class EweVocabulary(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	word = db.Column(db.String(64), nullable=False)
	category = db.Column(db.String(64), db.ForeignKey('category.name'), nullable=False)
	lexical_classes = db.relationship('LexicalClass', secondary=lexical_classes, lazy='dynamic', backref=db.backref('ewe_vocabulary', lazy='dynamic'))
	grammar_types = db.relationship('GrammarType', secondary=grammar_types, lazy='dynamic', backref=db.backref('ewe_vocabulary', lazy='dynamic'))
	audio = db.Column(db.String(240), nullable=True)
	image = db.Column(db.String(240), nullable=True)
	english_words  = db.relationship('EnglishWords', backref='ewe_vocabulary', lazy='dynamic')

class LexicalClass(db.Model):
	name = db.Column(db.String(64),  primary_key=True)

class GrammarType(db.Model):
	name = db.Column(db.String(64),  primary_key=True)

class EnglishWords(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	word = db.Column(db.String(64), nullable=False)
	ewe_vocab_id = db.Column(db.Integer, db.ForeignKey('ewevocabulary.id'))


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