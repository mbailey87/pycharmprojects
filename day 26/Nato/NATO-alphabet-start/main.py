# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

nato_csv = pandas.read_csv('nato_phonetic_alphabet.csv')
new_df = pandas.DataFrame(nato_csv)
#
new_dic = {row.letter: row.code for _ ,row in new_df.iterrows()}
# for (index,row) in new_df.iterrows():
#     new_dic.update({row.letter: row.code})

print(new_dic.get('A'))


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("type a word\n").upper()

word_list = [letter.upper() for letter in word]
# nato_word_list = [letter for letter in word_list]
nato_word_list = [new_dic[norm_letter] for norm_letter in word_list if norm_letter in new_dic]
# for norm_letter in word_list:
#     # a = new_df[new_df["letter"] == norm_letter]
#     # nato_word_list.append(a.code.item())
#     a = new_df[new_df["letter"] == norm_letter].code.item()
#     nato_word_list.append(a)

print(nato_word_list)



