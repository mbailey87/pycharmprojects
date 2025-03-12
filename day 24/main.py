# file = open("my_text.txt")
# contents = file.read()
# print(contents)
# file.close()

with open('my_text.txt', mode='a') as file: # this way you dont need to close the file
    file.write("\nHello World 2")


with open('my_text.txt') as file: # this way you dont need to close the file
    contents = file.read()
    print(contents)