print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age < 12:
        print("that will be 5 Dollars")
    elif age >= 12 and age <= 17:
        print("That will be 7 Dollars")
    else:
        print("That will be 12 dollars")
else:
    print("Sorry you have to grow taller before you can ride.")
