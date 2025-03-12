def greet(name):
    print(f'hey {name}')
    print(f'hello {name}')
    print(f'hi {name}')

greet('jack')

year = 52
total_weeks = year * 90



def weeks_left(age):
    your_age = age * 52
    total_weeks_left = (total_weeks - your_age)
    print(f'you have {total_weeks_left} weeks left')


weeks_left(30)