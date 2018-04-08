from app import db
from app.models import Category, Vocab, English, Lexical, Grammar, vocab_english_assoc
import sys
import json

db.create_all()

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

		for category, category_value in self.vocab_content.items():
			# check if category exists
			print(category)
			cat_exist = db.session.query(Category.name).filter(Category.name==category).count()
			print(cat_exist)

			# add new Category record
			if not cat_exist:
				cdb = Category(name=category)
				db.session.add(cdb)
				print(cdb)

			for vocab in category_value:
				# retrieve Vocab ID if word already exists in database
				for ee in vocab["ewe"]:
					vocab_db_id = db.session.query(Vocab.id).filter(Vocab.ewe==ee).count()

					# if vocab is not in database, create new Vocab record
					if not vocab_db_id:
						vocabdb = Vocab(ewe=ee, category=category, lexical=vocab["lexical"], audio=vocab["audio"], image=vocab["image"])

						for en in vocab["eng"]:
							eng_exist = db.session.query(English.word).filter(English.word==en).count()
							if not eng_exist:
								engdb = English(word=en)
								db.session.add(engdb)
							vocabdb.english_words.append(en)

						for gram in vocab["type"]:
							gram_exist = db.session.query(Grammar.name).filter(Grammar.name==gram).count()
							if not gram_exist:
								gramdb = Grammar(name=gram)
								db.session.add(gramdb)
							vocabdb.grammar_types.append(gram)

						db.session.add(vocabdb)
					
					else: # if vocab with matching ewe word is in databse

						lex_exist = db.session.query(Lexical.name).filter(Lexical.name==vocab["lexical"]).count()

						if not lex_exist:
							lexdb = Lexical(name=vocab["lexical"])
							vocabdb = Vocab(ewe=ee, category=category, lexical=vocab["lexical"], audio=vocab["audio"], image=vocab["image"])

							db.session.add(lexdb)
							db.session.add(vocabdb)

						else:
							# check if here is a Vocab record with same ewe and same lexical fields
							vocabdb = db.session.query(Vocab).filter(Vocab.ewe==ee, Vocab.lexical==vocab["lexical"])
		#TEST
							if vocabdb.count():

								for en in vocab["eng"]:
									eng_exist = db.session.query(English).filter(English.word==en).count()

									#if en is not in database, add English record and add to english_words
									if not eng_exist:
										engdb = English(word=en)
										db.session.add(engdb)
										vocabdb.first().english_words.append(en)
									else:
										en_in_vocab = db.session.query(Vocab).filter(en in Vocab.english_words).count()
										if not en_in_vocab:
											vocabdb.first().english_words.append(en)

								for typ in vocab["type"]:
									gram_exist = db.session.query(Grammar).filter(Grammar.name==typ).count()

									if not gram_exist:
										gramdb = Grammar(name=typ)
										db.session.add(gramdb)
										vocabdb.first().grammar_types.append(typ)
									else:
										typ_in_vocab = db.session.query(Vocab).filter(typ in Vocab.grammar_types).count()
										if not typ_in_vocab:
											vocabdb.first().grammar_types.append(typ)

		#db.session.commit()

	def check_exists(self, condition):
		record_id = db.session.query(exists().where(condition))
		return record_id


#dp = dictionary_parser("C:\\Users\\mawusi\\Dropbox\\Ewe_Project\\learnapp\\lesson_data\\vocabulary_test.json")
dp = dictionary_parser("D:\\Dropbox\\Ewe_Project\\learnapp\\lesson_data\\vocabulary_test.json")

dp.create_vocabulary_db()