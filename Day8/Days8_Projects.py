# Caeser Cipher
from art import logo

# Creating Functions
def cipher(text,position,mode):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    cipher = ""
    if mode == "decode":
        position *= -1
    for char in text:
        if char not in alphabet:
            cipher+=char
        else:
            get_index = alphabet.index(char)
            get_index+=position
            get_index%=len(alphabet)
            cipher+=alphabet[get_index]

    print(f"\nYour {mode}d text is: {cipher}")

# Main Code

print("\n----------------Welcome to Caeser Cipher-------------------")
print(logo)
repeat = "yes"
while repeat == "yes":
    mode = input("\nWhat do you want, 'encode' or 'decode'? : ").lower()
    user_text = input("Enter your text : ")
    position_shift = int(input("How much position you want to shift in your cipher text? : "))
    cipher(user_text,position_shift,mode)    # Calling Function
    repeat = input("\nAre you want to repeat again? : 'yes' or 'no': ")
print("\nGood Bye")
