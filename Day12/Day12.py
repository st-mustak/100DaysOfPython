#Checking a number prime or not

def is_prime(num):
    if num<=1:
        return False
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(f"The number is divisible by {i}")
                return False

                break
        else:
            return True

while input("\n\n\nDo you want to check a number prime or not?\n Type 'y' for Yes and 'n' for No: ") == 'y':
    a= is_prime(int(input("Enter a number: ")))
    if a==True:
        print("It's a prime number.")
    else:
        print("So, It's not a prime number.")