# def odd_or_even(number):
#     if number % 2 == 0:
#         print("This is an even number.")
#     else:
#         print ("This is an odd number.")
# odd_or_even(3)
# odd_or_even(4)
# odd_or_even(3)
# odd_or_even(2)
# odd_or_even(3)

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
fizz_buzz(50)