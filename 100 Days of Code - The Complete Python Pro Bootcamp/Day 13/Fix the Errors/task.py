try:
    age = int(input("How old are you?"))
except ValueError:
    print("please enter a number")
    age = int(input("How old are you?"))
if age < 18:
    print(f"You can drive at age 18.")
elif age >= 18:
    print(f"You are {age} years old. You can drive!")
