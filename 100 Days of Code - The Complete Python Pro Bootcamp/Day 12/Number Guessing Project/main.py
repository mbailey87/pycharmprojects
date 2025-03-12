import random

NUMBER = random.randint(1,100)
print(NUMBER)
def play_game():
    guesses = 0
    level = ''
    while guesses == 0:
        level = input("Choose a difficulty level 'easy' or 'hard'\n").lower()
        if level == 'easy':
            guesses = 10
        elif level == 'hard':
            guesses = 5
        else:
            print("choose 'easy' or 'hard'")

    while guesses > 0:
        print(f"you chose {level} you have {guesses} chances to guess the number")
        guess = int(input("Guess a number from 1 to 100\n"))
        if guess == NUMBER:
            print("you win!")
            break
        elif guess > NUMBER:
            print("you guessed to high")
            guesses -= 1
        else:
            print("you guessed to low")
            guesses -= 1

    if guesses == 0:
        print("you have 0 guesses left you lose")

play_game()