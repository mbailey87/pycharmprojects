#TODO: Create a letter using starting_letter.txt



#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    names_text = names.read()
    print(names_text)
    name_list = names_text.split("\n")

print(name_list)
#Replace the [name] placeholder with the actual name.
for name in name_list:
    with open('./Input/Letters/starting_letter.txt') as starting_text:
        old_letter = starting_text.read()
        new_string = old_letter.replace("[name]", f"{name}")
        print(new_string)

        with open(f'./Output/ReadyToSend/letter_{name}.txt', mode="w") as letter:
            letter.write(new_string)





#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp