# Tip Calculator

print("Welcome to Tip Calculator")

bill = float(input("What is the Total Bill? $"))
tip_per = int(input("What percent tip would you like to give? 10 12 15"))
people =  int(input("How many people to split the bill?"))
tip = bill*tip_per/100
total_bill = bill + tip

bill_per_person = total_bill/people

final_amount = round(bill_per_person,2)

print(f"Each person should pay: $ {final_amount}")

#Done



