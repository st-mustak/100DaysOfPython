import menu
report_amount = 0

def is_resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= menu.resources[item]:
            print("Insufficient Ingredients.")
            return False
        return True

def payment():
    print("Please, Insert Coins to get your drink.")
    total = int(input("How many 10 Rupees?: "))*10
    total+=int(input("How many 5 Rupees?: "))*5
    total+=int(input("How many 2 Rupees?: "))*2
    total+=int(input("How many 1 Rupees?: "))*1
    print(f"You have deposited {total} Successfully.")
    return total

def transaction_status(payment_received,drink_value):
    if payment_received>= drink_value:
        refund_amount = payment_received-drink_value
        global report_amount
        report_amount+=drink_value
        print(f"Congarts! Your order has been placed successfully. Your remaining wallet balance is {refund_amount}.")
        return True
    else:
        print(f"Insufficient Money. Your have refunded successfully.")
        return False

def preparing_coffee(drink, order_ingredients):
    for item in order_ingredients:
        menu.resources[item] -= order_ingredients[item]
    print(f"Enjoy your Drink {drink}")


loop_on = True

while loop_on:
    user_input=input("What you would like ? (espresso/latte/cappuccino): ")
    if user_input=="off":
        loop_on = False
    elif user_input == "report":
        print(f"Your Drink: {user_input}")
        print(f"Water: {menu.resources['water']}")
        print(f"Milk: {menu.resources['milk']}")
        print(f"Coffee: {menu.resources['coffee']}")
        print(f"Drink Price: {report_amount}")
    else:
        drink = menu.MENU[user_input]
        if is_resource_available(drink['ingredients']):
            payment_amount = payment()
            if transaction_status(payment_amount,drink['cost']):
                preparing_coffee(user_input,drink['ingredients'])
            else:
                print("You don't have sufficient money.Your money has been refunded successfully.")








