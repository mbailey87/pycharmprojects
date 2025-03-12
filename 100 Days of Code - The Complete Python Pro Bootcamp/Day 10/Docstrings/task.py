# doc strings are documentation for your code while you code you use three ""

def format_name(f_name, l_name):
    """Take a first and last name and format it to title case""" # must be on the first line after defining the function
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)



