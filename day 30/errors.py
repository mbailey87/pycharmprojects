# FileNotFound
# with open('a_file.text') as file:
#     file.read()

# KeyError
# a_dictionary = {"key": 'Value'}
# value = a_dictionary['non_existant_key']

# IndexError index does not exist
# fruits = ['apple','pear','peach']
# fruit = fruits[3]

# TypeError
# text = 'abc'
# print(text + 5)

# try: something that might cause an exception
#
# except: do this if there was an exception
#
# else: if no exceptions do this
#
# finally: do no matter what

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": 'Value'}
#     print(a_dictionary['non_existant_key'])
# except FileNotFoundError:
#     print('there was an error')
#     file = open("a_file.txt", 'w')
# except KeyError as error_message:
#     print(f'that key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
#
# finally:
#     file.close()
#     print('file was closed')
#     raise TypeError('THis is an error')


height = float(input('Height: '))
weight = int(input('weight: '))

if height > 3:
    raise ValueError('most humans ar not over 3 meters tall')

bmi = weight / height ** 2

print(bmi)

