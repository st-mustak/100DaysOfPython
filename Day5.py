#for loops
# fruits = ["Orange","Guava","Bananas","Apple"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)
# --------------------------------------------
# # adding all list items using function
# student_scores = [234,134,523,121,321,34,123,534,344,523]
# total_scores = sum(student_scores)
# print(total_scores)
# -------------------------------------------------
# # adding all list items using for loop
# student_scores = [234,134,523,121,321,34,123,534,344,523]
# sum = 0
# for score in student_scores:
#     sum+=score
# print(sum)
# --------------------------------------------------------
# #calculate max score using max() function
# student_scores = [234,134,523,121,321,34,123,534,344,523]
# max_score = max(student_scores)
# print(max_score)
# -----------------------------------------------------------
# #calculate max score using loop
# student_scores = [234,134,523,121,321,34,123,534,344,523]
# max_score = 0
# for score in student_scores:
#     if score>max_score:
#         max_score=score
# print(max_score)
# ---------------------------------------------------------------

# #Range in Loops
# for number in range(1,11, 2):
#     print(number)

# # Sum of first 100 numbers
# total  = 0
# for number in range(1,101):
#     total+=number
# print(total)

# #Fizz-Buzz Game
# for number in range(1,101):
#     if number%3==0 and number%5==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)