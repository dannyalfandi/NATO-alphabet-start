student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
get_nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

list_nato_phonetic_alphabet = {row.letter:row.code for (index, row) in get_nato_phonetic_alphabet.iterrows()}
{"A": "Alfa", "B": "Bravo"}

# result = [value for (key, value) in list_nato_phonetic_alphabet.items()]

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_done = False
while not is_done:
    name_inputs = input("If you want to close, type exit. Enter a word: ").upper()
    if name_inputs == "EXIT":
        is_done = True
    else:
        list_name = list(name_inputs)

        result = [list_nato_phonetic_alphabet[letter]
                  for letter in list_name
                  if letter in list_nato_phonetic_alphabet]

        print(result)
