from app import db
from app.models import EweVocabulary, EnglishWords, LexicalClass, GrammarType
import sys
import json

class dictionary_parser:
	def __init__(self, dict_file):
		#Read in json vocab file
		try:
		    with open(dict_file, encoding='utf-8') as json_content:  # UTF-8 encoding for special latin characters
		        self.vocab_content = json.load(json_content)
		except json.decoder.JSONDecodeError:
		    print('The given JSON input file is invalid. Try validating it at https://jsonlint.com.')
		    sys.exit(0)

	def create_vocabulary_db(self):

		cat_db = []
		eng_db = []
		lex_db = []
		typ_db = []

		vocab_db = []

		vocab_lex_db = []
		vocab_typ_db= []

		vocab_id = 0

		for category, category_value in self.vocab_content.items():
			cat_db.append(category)

			for vocab in category_value:
				ee = vocab["ewe"][0]
				
				for en in vocab["eng"]:
					eng_db.append(dict(vocab_ID=vocab_id, eng=en))

					for lex in vocab["lexical"]:
						if lex not in lex_db:
							lex_db.append(lex)
						vocab_lex_db.append(dict(vocab_ID=vocab_id, lexical=lex))

						for typ in vocab["type"]:
							if typ not in typ_db:
								typ_db.append(typ)
							vocab_typ_db.append(dict(vocab_ID=vocab_id, type=typ))

				vocab_db.append(dict(id=vocab_id, ewe=ee, category=category, audio=vocab["audio"], image=vocab["image"]))

				vocab_id = vocab_id + 1

		for unit in vocab_db:
			print(unit)

	def add_database_entry(self, values, databse_name):
		pass

	def create_sentence_db(self):
		pass
	"""
	Read in json sentence file
	    for each dictionary item 
	        add to DB

	"""

dp = dictionary_parser("C:\\Users\\mouse\\Dropbox\\Ewe_Project\\learnapp\\lesson_data\\vocabulary_test.json")

dp.create_vocabulary_db()