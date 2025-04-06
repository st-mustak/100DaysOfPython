# Python Primitive Data Type

# Printing Character of a string
print("Hello"[3])

# Printing the last Character
print("Hello"[-1])

# Note: -ve symbol use to take character from the last

# String Concatenation

print("Mustak"+ "Ahmed")

# Interger = Whole Number

print(123+431)

# Large Integer for example 70,000

print(70_000)

# Float Number

print(3.14543)

# Boolean
print(True)
print(False)


# Type Error, Type Checking

print(type("Hi"))
print(type(7465))
print(type(3445.6343))
print(type(True))

 # Type Conversion
print(int("100")+int("50"))
#
# # nameOfUser = input("Enter Your Name: ")
# # lengthOfName = len(nameOfUser)
# print(type("Number of letter in your name : "))
# print(type(lengthOfName))
#
# print("Number of letter in your name is :" + str(lengthOfName))

# Mathematical Operation


print(100+55)
print(100-50)
print(4*8)
print(5/3) #Return Float Value
print(6//2) #Return Integer Value
print(2**3) #Power Value

# PEMDAS - Parenthesis > Exponent> Multiplication > Division > Addition/Substraction

# ()
# **
# * OR /
# + OR -

print(3*3+3/3-3)  #Calculation are from left to right for the same order
# 3*3+3/3-3 = 9+3/3-3  = 9+1-3 = 10-3 = 7

print(3*(3+3)/3-3) # 3*6/3-3 = 18/3-3 = 6-3 = 3

#Rounding

weight = 84
height = 1.65

bmi = weight/height**2

print(bmi)
print(round(bmi))
print(round(bmi,2))

#Assignment Operator

score = 2
score +=1
print(score)

#F-String

# print("Your Score is: " + str(score))

print(f"Your Score is: {score}")