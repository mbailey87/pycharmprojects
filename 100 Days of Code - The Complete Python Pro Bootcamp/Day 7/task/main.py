import random
import hangman_words
import hangman_art
#
# # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#
# lives = 6
#
# # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)
#
# game_over = False
# correct_letters = []
#
# while not game_over:
#
#     # TODO-6: - Update the code below to tell the user how many lives they have left.
#     print("****************************<???>/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()
#
#     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#
#     display = ""
#
#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#
#     print("Word to guess: " + display)
#
#     # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#     #  e.g. You guessed d, that's not in the word. You lose a life.
#
#     if guess not in chosen_word:
#         lives -= 1
#
#         if lives == 0:
#             game_over = True
#
#             # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
#             print(f"***********************YOU LOSE**********************")
#
#     if "_" not in display:
#         game_over = True
#         print("****************************YOU WIN****************************")
#
#     # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
#     print(stages[lives])


chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for letter in chosen_word:
    placeholder += '_'
print(placeholder)
display = ''
placeholder = list(placeholder)
lives = 6
not_letters = ''

print(hangman_art.logo)
print(f'Welcome to hangman you have {lives}/6 lives guess to guess the word')
# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
while display != chosen_word and lives > 0:

    guess = input("Guess a letter: ").lower()

    if guess.isdigit():
        print("Please guess a letter not a number.")
    if len(guess) > 1:
        print('Please choose only one letter.')
    if guess in display or not_letters:
        print('You have already guessed that. Try a different letter')
    if guess in chosen_word:
        for (index, letter) in enumerate(chosen_word):
            if letter == guess:
                placeholder[index] = guess
    if guess not in chosen_word and guess not in not_letters and len(guess) == 1 and not guess.isdigit():
        lives -= 1
        print(f'you have {lives}/6 lives left.')
        not_letters += guess



    display = ''.join(placeholder)
    print(display)
    print(hangman_art.stages[lives])



if lives == 0 and display != chosen_word:
    print("You Loose")
elif display == chosen_word:
    print("You Win")