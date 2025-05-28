# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"{formatted_f_name} {formatted_l_name}"
#
# user_name = format_name("muStak","ahMed")
# print(user_name)



# Leap-Year Calculator
def is_leap_year(year):

    leap_year = "Not Leap-Year"
    if year % 4 == 0:
        leap_year = "Leap-Year"
        if year % 100 == 0:
            leap_year = "Not Leap-Year"
            if year % 400 == 0:
                leap_year = "Leap-Year"
                return leap_year
            return leap_year
        return leap_year
    return leap_year
user_input = input("Enter a Year : ")
numbers = ["0","1","2","3","4","5","6","7","8","9"]

is_true = True
user_input_final = ""
for c in user_input:
    if c in numbers:
        user_input_final+=c
    else:
        is_true = False
print(is_leap_year(int(user_input_final))) if is_true is True and int(user_input_final)>0 else print("I know you are Ukil, That's why computer gets Error.")


# Docstring
"""This is Documents or Multi-line Commands"""