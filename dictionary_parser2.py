from app import db
from app.models import Category, Vocab, English, Lexical, Grammar
import sys
import json

db.create_all()

GRAMMAR_TYPES = []
LEXICAL_CLASSES = ['sentence', 'noun', 'verb', 'adjective', 'adverb', 'determiner']

class dictionary_parser:
	def __init__(self, dict_file):
		#Read in json vocab file
		try:
			with open(dict_file, encoding='utf-8') as json_content:  # UTF-8 encoding for special latin characters
				self.vocab_content = json.load(json_content)
		except json.decoder.JSONDecodeError:
			print('The given JSON input file is invalid. Try validating it at https://jsonlint.com.')
			sys.exit(0)

	def eng_check(self, englist, vocab):
		for en in englist:
			engdb = db.session.query(English).filter(English.word==en).first()

			if not engdb:
				engdb = English(word=en)
				db.session.add(engdb)
				print("New English added: {}".format(engdb))

			if vocab:
				en_in_vocab = db.session.query(Vocab).filter(en in vocab.english_words).count()
				if not en_in_vocab:
					vocab.english_words.append(engdb)
					if vocab.id:
						print("<Vocab: ID {}> updated with {}".format(vocab.id, engdb))

	def gram_check(self, gramlist, vocab):
		for gram in gramlist:
			gramdb = db.session.query(Grammar).filter(Grammar.name==gram).first()

			if not gramdb:
				gramdb = Grammar(name=gram)
				db.session.add(gramdb)
				print("New Grammar added: {}".format(gramdb))

			if vocab:
				gram_in_vocab = db.session.query(Vocab).filter(gram in vocab.grammar_types).count()
				if not gram_in_vocab:
					vocab.grammar_types.append(gramdb)
					if vocab.id:
						print("<Vocab: ID {}> updated with {}".format(vocab.id, gramdb))

	def create_vocabulary_db(self):

		for category, category_value in self.vocab_content.items():
			# check if category exists
			cat_exist = db.session.query(Category.name).filter(Category.name==category).count()

			if cat_exist:
				print("Category: {} already exists".format(cdb))

			# add new Category record
			if not cat_exist:
				cdb = Category(name=category)
				db.session.add(cdb)
				print("New Category added: {}".format(cdb))

			for vocab in category_value:
				# retrieve Vocab if Vocab with with corresponding ewe and lexical fields exists in database
				for ee in vocab["ewe"]:
					vocabdb = db.session.query(Vocab).filter(Vocab.ewe==ee, Vocab.lexical==vocab["lexical"]).first()

					# if Vocab is not in database
					if not vocabdb:

						# check for existence of Lexical record
						lexdb = db.session.query(Lexical).filter(Lexical.name==vocab["lexical"]).first()

						if not lexdb:
							lexdb = Lexical(name=vocab["lexical"])
							db.session.add(lexdb)
							print("New Lexical Class added: {}".format(lexdb))

							# create new Vocab record
							vocabdb = Vocab(ewe=ee, category=category, lexical=vocab["lexical"], audio=vocab["audio"], image=vocab["image"])

							# check for existence of English and Grammar records and update the corresponding Vocab fields
							self.eng_check(vocab["eng"], vocabdb)
							self.gram_check(vocab["type"], vocabdb)

							db.session.add(vocabdb)
							print("New Vocab added: {} \n".format(vocabdb))

						else:
							print("{} already exists".format(lexdb))

							# create new Vocab record
							vocabdb = Vocab(ewe=ee, category=category, lexical=vocab["lexical"], audio=vocab["audio"], image=vocab["image"])

							# check for existence of English and Grammar records and update the corresponding Vocab fields
							self.eng_check(vocab["eng"], vocabdb)
							self.gram_check(vocab["type"], vocabdb)

							db.session.add(vocabdb)
							print("New Vocab added:	{} \n".format(vocabdb))
					
					else: # if Vocab with corresponding ewe and lexical is in database

						print("<Vocab: ID {},  Ewe \"{}\",  Lexical \"{}\"> already exists \n".format(vocabdb.id, vocabdb.ewe, vocabdb.lexical))

						# check for existence of English and Grammar records and update the corresponding Vocab fields
						self.eng_check(vocab["eng"], vocabdb)
						self.gram_check(vocab["type"], vocabdb)

		#db.session.commit()

#dp = dictionary_parser("C:\\Users\\mawusi\\Dropbox\\Ewe_Project\\learnapp\\lesson_data\\vocabulary_test.json")
dp = dictionary_parser("D:\\Dropbox\\Ewe_Project\\learnapp\\lesson_data\\vocabulary_test.json")

dp.create_vocabulary_db()