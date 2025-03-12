import game_data, random, art

def game():
    options = [random.choice(game_data.data), random.choice(game_data.data)]
    if options[0] == options[1]:
        options[1] = random.choice(game_data.data)
    score = 0
    print(art.logo)

    def print_details():
        print(f"Your score: {score}")
        print(f"Option A: {options[0]["name"]} a {options[0]["description"]} from {options[0]["country"]}")
        print(art.vs)
        print(f"Option B: {options[1]["name"]} a {options[1]["description"]} from {options[1]["country"]}")

    def correct_choice(num):
        options.append(random.choice(game_data.data))
        num += 1
        print("\n" * 100, art.logo)
        print("Correct!")
        return num
    play_again = True

    while play_again:
        print_details()
        guess = input("Who has more followers 'A' or 'B' \n").lower()
        if guess == 'a':
            if options[0]["follower_count"] > options[1]["follower_count"]:
                del options[1]
                score = correct_choice(score)
                continue
            else:
                print(f"Wrong. Your final score is:{score}")
                break

        if guess == 'b':
            if options[0]["follower_count"] < options[1]["follower_count"]:
                del options[0]
                score = correct_choice(score)
                continue
            else:
                print(f"Wrong. Your final score was: {score}")
                break
        else:
            print("Please choose 'A' or 'B'")
game()