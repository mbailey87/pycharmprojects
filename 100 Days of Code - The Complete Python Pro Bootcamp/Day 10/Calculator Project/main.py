import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# print(operations['+'](2,4))

continue_program = True
n1 = float(input("what's the first number?: \n"))
def op_sec_num():
    operation = input("+\n-\n*\n/\npick an operation:")
    n2 = float(input("what's the second number?: \n"))
    return operation, n2
operation, n2 =op_sec_num()
total = 0
while continue_program:

    total = operations[operation](n1,n2)
    # if operation == "+":
    #    total =  add(n1, n2)
    # elif operation == "-":
    #    total = subtract(n1, n2)
    # elif operation == "*":
    #    total = multiply(n1, n2)
    # elif operation == "/":
    #    total = divide(n1, n2)
    # else:
    #     print('please try again with a valid operator')
    #     operation, n2 = op_sec_num()


    print(f'{n1} {operation} {n2} = {total}')
    next_calculation = input("press 'y' to continue or 'n' do a new calculation or 'exit' to exit program. \n").lower()
    if next_calculation == 'n':
        print("\n" * 100)
        print(art.logo)
        n1 = int(input("what's the first number?: \n"))
        operation, n2 = op_sec_num()
        continue
    if next_calculation == 'y':
        n1 = total
        operation, n2 = op_sec_num()
        continue
    if next_calculation == 'exit':
        print('Thank you')
        continue_program = False
