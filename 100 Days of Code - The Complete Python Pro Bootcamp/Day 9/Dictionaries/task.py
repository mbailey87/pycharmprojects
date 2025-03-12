# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary["Bug"])
#
# programming_dictionary['Loop'] = 'something run over and over again'
# programming_dictionary['Bug'] = 'a moth in your pc'
# print(programming_dictionary)
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# programming_dictionary = {}
# print(programming_dictionary)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for key in student_scores:
    if student_scores[key] >= 91:
        student_scores[key] = 'Outstanding'
    elif 81 <= student_scores[key] < 91:
        student_scores[key] = 'Exceeds Expectations'
    elif 71 <= student_scores[key] < 81:
        student_scores[key] = 'Acceptable'
    else:
       student_scores[key] = 'Fail'


student_grades = student_scores

print(student_grades)