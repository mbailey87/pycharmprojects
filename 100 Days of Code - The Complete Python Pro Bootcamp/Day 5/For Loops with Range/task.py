# total = 0
# for number in range(1,101): # range(start, >end, increment(defaults to 1))
#     total += number
# print(total)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)
