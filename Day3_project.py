# Treasury Island Project
#
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************

print("Welcome to Treasure Island.")
print("Your Mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do '
                'you want to go? Type "left" or "right": ').lower()
if choice1 == 'left' :
    choice2 = input('You\'ve come to a lake.There is an '
                    'island in the middle of the lake. '
                    'Type "wait" to wait for a boat'
                    ' ot Type "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island safely.'
              ' There is an house with 3 doors. '
              'One red, one blue and another is yellow, which door you choose : ' ).lower()
        if choice3== "red" :
            print("You\'ve entered a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You\'ve entered in a room of beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the Treasure. You Win!")
        else:
            print("You got attacked by an angry trout.Game Over.")
elif choice1 == "right":
    print('You fell into a hole. Game Over.')
else:
    print("You entered Wrong Input")

