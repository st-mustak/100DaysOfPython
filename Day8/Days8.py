# def greet():
#     print("****  You make only Function and called it ****")
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?\n")
#
# greet()
#
## Functions with 1 parameter
# def greet_with_name(name):
#     print("****  You make Function with parameter and called it ****")
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice {name}?")
#
# greet_with_name("Mustak")

# # Exercise
# # Calculating time left to live
# def life_in_weeks(user_input):
#     weeks_left =  (90 - user_input) * 52
#     print("Assuming you will live 90 years.")
#     print(f"Your Current Age is : {user_input} years old.")
#     print(f"You have {weeks_left} weeks left.")
# repeat = 'y'
# while repeat == "y":
#     age = int(input("\nEnter Your Age ( in Years ): "))
#     life_in_weeks(age)
#     repeat= input("\nAre you want to repeat this process?\nEnter "
#                   "'y' for Yes and 'n' for No : ")
# print("\nThanks for using me.")
#
# # Functions with 2 parameters
# def greet_with(name,location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")
#
# greet_with("Banglore","Mustak Ahmed")
# greet_with(location="Banglore", name = "Mustak")


# Exercise
# Love Score Calculator
#
#  To work out the love score between two people:
#
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# 2. Then check for the number of times the letters in the word LOVE occurs.
#
# 3. Then combine these numbers to make a 2 digit number and print it out.

def calculate_love_score(name1, name2):
    name = name1.lower() + name2.lower()
    a = 0
    for letter in name:
        for char in "true":
            if char == letter:
                a += 1
    b=0
    for letter in name:
        for char in "love":
            if char == letter:
                b += 1
    print(f"\nYour Love Score is: {a}{b}")

name1 = input("Enter Your Name : ")
name2 = input("Enter Your Loved Person's Name : ")

calculate_love_score(name1,name2)