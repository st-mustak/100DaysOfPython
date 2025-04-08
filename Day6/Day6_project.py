# Reborg's Maze Game


# **** Defining All the Functions ****

def right_is_clear():
    print("Right is Clear")
def front_is_clear():
    print("Front is Clear")
def wall_on_right():
    print("Wall_on_right")
def wall_in_front():
    print("")
def at_goal():
    print("At Goal")
def move():
    print("Move")
def turn_left():
    print("Turn Left")
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()




