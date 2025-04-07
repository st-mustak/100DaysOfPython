# Functions

# 1. Defining Function
# 2. Executing Function / Call a Function

#Defining Function
#
# def myFunction():
#     print("This Function is created by me.")
# myFunction()
#
#
# def turn_left():
#     print("")
# def move():
#     print("")
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def one_hurdle():
#
# move()
# turn_left()
# turn_right()
# turn_right()
# turn_left()




# ************   ReeBorg's Hurdle   ************


# **** Defining All the Functions ****
# def front_is_clear():
#     print("Front is Clear")
# def wall_on_right():
#     print("Wall_on_right")
# def wall_in_front():
#     print("")
# def at_goal():
#     print("At Goal")
# def move():
#     print("Move")
# def turn_left():
#     print("Turn Left")
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# ---------------------------------------------

# **** Goal after 6 Walls ****
# Calling jump() function Repeatedly
# jump()
# jump()
# jump()
# jump()
# jump()
# jump()

# Using For Loops
# for step in range(6):
#     jump()

# Using While Loops
# no_of_jump = 6
# while no_of_jump >0:
#     jump()
#     no_of_jump -=1

# ----------------------------------------------

# **** Random Goal-Post ****
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while at_goal() != True :
#     jump()
# ----- Or ------
# while not at_goal():
#     jump()

# ------------------------------------------------

# **** Random Wall ****
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# ------------------------------------------------

# **** At Random Height of Wall ****
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()