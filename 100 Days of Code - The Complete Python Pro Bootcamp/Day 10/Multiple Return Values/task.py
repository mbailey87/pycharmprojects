# def format_name(f_name, l_name):
#     if f_name == '' or l_name == '':
#         return "You did not provide valid input"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# output = format_name(input("what is your first name"), input('what is your last name'))
# print(output)

def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"

output = is_leap_year(2000)
print(output)
