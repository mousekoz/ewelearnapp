# challenge ID, user ID, number of times accessed, number of times incorrect, difficulty
from app import models
import random

class Challenge:
    def __init__(self, languages, challenge_input):

        # Variables to hold L1 and L2 names and code keys
        self.lang_name_1 = languages['L1']["name"]
        self.lang_name_2 = languages['L2']["name"]
        self.lang_code_1 = languages['L1']["code"]
        self.lang_code_2 = languages['L2']["code"]

        self.challenge_input = challenge_input

    def intro_challenge(self, element_id):   # Takes in a dict of phrase/sentence
        
        # Looks up element using ID argument
        current_element = self.challenge_input[element_id]
        # Print the first Ewe phrase in list
        print("\n{}: ".format(lang_name_2) + current_element[lang_code_2][0])
        # Print the first English phrase in list
        print("{}: ".format(lang_name_1) + current_element[lang_code_1][0] + "\n")
        # Take user input
        user_ans = input("What is '{}' in {}?: ".format(current_element[lang_code_2][0], self.lang_name_1))

        # Check whether user input is in list of correct answers
        # Compare in a case-insensitive manner
        is_correct = user_ans.lower() in [w.lower() for w in current_element["eng"]]

        if is_correct:
            # if correct and difficulty value greater than 0, subtract 1
            if current_element['difficulty'] > 0:
                current_element['difficulty'] = current_element['difficulty'] - 1
            print("Correct.")
            # If the user used a different word that is also in the the list
            if user_ans != current_element["eng"][0]:
                print("Remember - '{}' also means '{}'!".format(current_element[lang_code_2][0],
                                                                current_element[self.lang_code_1[0]]))
        else:
            # if incorrect, show correct word - if difficulty value less than 3, add 1
            if current_element['difficulty'] < 3:
                current_element['difficulty'] = current_element['difficulty'] + 1
            print("Incorrect - '{}' means '{}' in English.".format(current_element[lang_code_2][0],
                                                                   [self.lang_code_1[0]]))

        # Update quiz dictionary with new stat
        current_element["L2_intro"] = 1

    def trans_challenge(self, element_id, is_default=True):
        current_element = self.challenge_input[element_id]

        # Function variables to handle both L2-L1 and L1-L2 translation
        if is_default:
            trans_lang_name_1 = self.lang_name_1
            trans_lang_code_1 = self.lang_code_1
            trans_lang_code_2 = self.lang_code_2
        else:
            trans_lang_name_1 = self.lang_name_2
            trans_lang_code_1 = self.lang_code_2
            trans_lang_code_2 = self.lang_code_1

        user_ans = input("Type '{}' in {}: ".format(current_element[trans_lang_code_2][0],
                                                    trans_lang_name_1))

        # TODO: look into 'fstring literal' - "Type '{current_element[self.language[input_lang][1]][0]}'
        # TODO: in {self.language[output_lang][0]}: "

        # Check whether user input is in list of correct answers
        # Compare in a case-insensitive manner
        is_correct = user_ans.lower() in [w.lower() for w in current_element[trans_lang_code_1]]

        if is_correct:
            # If correct answer is input and difficulty value greater than 0, subtract 1
            if current_element['difficulty'] > 0:
                current_element['difficulty'] = current_element['difficulty'] - 1
            print("Correct.")

        else:
            # If incorrect answer is input and difficulty value less than 3, add 1
            # and show correct answer
            if current_element['difficulty'] < 3:
                current_element['difficulty'] = current_element['difficulty'] + 1
            print("Incorrect.")

        # Update quiz dictionary with new stat
        if is_default:
            current_element["L2_trans"] = 1
        else:
            current_element["L1_trans"] = 1

    def order_challenge(self, element_id):
        current_element = self.challenge_input[element_id]
        current_string = current_element[self.lang_code_2][0]
        # Break word into list of words
        split_list = current_string.split(" ")

        # Create a deep copy of the list to shuffle
        shuffle_list = list(split_list)

        # Make sure shuffled word order is different to original
        while split_list == shuffle_list:
            random.shuffle(shuffle_list)

        # Create a string of the shuffled sentence
        mixed_string = ' '.join(shuffle_list)

        print(mixed_string+"\n")

        user_ans = input("Put the words in the correct order: ")

        # Check whether user input matches original string
        # Compare in a case-insensitive manner
        is_correct = user_ans.lower() == current_string.lower()

        if is_correct:
            # If answer is correct and difficulty value greater than 0, subtract 1
            if current_element['difficulty'] > 0:
                current_element['difficulty'] = current_element['difficulty'] - 1

            print("That's correct. " + "\n\"" + current_element[self.lang_code_1][0] + "\"" + "\n")

        else:
            # If incorrect answer is input and difficulty value less than 3, add 1
            # and show correct answer
            if current_element['difficulty'] < 3:
                current_element['difficulty'] = current_element['difficulty'] + 1
            print("That's incorrect.")
            print("\""+current_string+"\"\n")

        current_element["L2_order"] = 1

    # function multiple_challenge
    def multiple_challenge(self, element_id):
        current_element = self.challenge_input[element_id]

        all_phrase_list = []
        all_phrase_dict = {}

        print(current_element[self.lang_code_2])

        for e_id, e_value in self.challenge_input.items():
            if e_value["phr_or_snt"] == "phrases":
                all_phrase_dict[self.lang_code_2] = e_value[self.lang_code_2]
                all_phrase_dict[self.lang_code_1] = e_value[self.lang_code_1]

                all_phrase_list.append(all_phrase_dict)

        word_choice_list = []
        for num in range(1, 5):
            random_num = random.randrange(0, len(all_phrase_list))

            while all_phrase_list[random_num] not in word_choice_list:
                random_num = random.randrange(0, len(all_phrase_list))

            word_choice_list.append(all_phrase_list[random_num])

        """
        choose a random selection of words
        compare user answer to selected word
        """


    # Print L1 word
    # Print a random selection of L2 words and the correct L2 word
    # Take user input
    # Compare the units
    # Record result
    # if correct and difficulty value greater than 0, subtract 1
    # if incorrect, show correct word - if difficulty value less than 3, add 1
    # Return true or false

"""
    # function blank_challenge
    def blank_challenge(self, element_id):
        current_element = self.challenge_input[element_id]
        current_string = current_element[self.lang_code_2][0]

        # Break word into list of words
        split_list = current_string.split(" ")

        output_list = []

        word_count = len(split_list)
        random_position = random.randrange(0, word_count)

        for num in range(0, word_count):
            if num is not random_position:
                output_list.append(split_list[num])
            else:
                output_list.append(" ___ ")

        output_string = ' '.join(output_list)

        print(output_string)

        all_phrase_list = []
        for e_id, e_value in self.challenge_input.items():
            if e_value["phr_or_snt"] == "phrases" and e_value["lexical"] != current_element["lexical"]:
                all_phrase_list.append(e_value[self.lang_code_2])

        random.shuffle(all_phrase_list)
        print(all_phrase_list)

        word_choice_list = []
        for num in range(1, 5):
            random_choice = random.randrange(0, len(all_phrase_list))
            while random_choice in word_choice_list:
                random_choice = random.randrange(0, len(all_phrase_list))

            word_choice_list.append(random_choice)

        print(word_choice_list)

    # Print L2 sentence with specific word missing
    # Print a specific selection of words and the correct word
    # Take user input
    # Compare the units
    # Record result
    # if correct and difficulty value greater than 0, subtract 1
    # if incorrect, show correct word - if difficulty value less than 3, add 1
    # Return true or false

"""
