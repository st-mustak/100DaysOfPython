import random

# print(random.uniform(1,10))
# print(random.random())


# # Random Head & Tail
# random_head_tail = random.randint(0,1)
# if random_head_tail == 0:
#     print("Head")
# else:
#     print("Tail")


# # List - Data Structure
# indian_states = ['West Bengal','Karnataka','Uttar Pradesh',
#                  'Bihar', 'Tamilnadu','Maharashtra', 'Kerala',
#                  'Jharkhand','Odissa']
# print(indian_states)
# indian_states[0] = 'Bangla'
# print(indian_states)
# indian_states.append('Jammu and Kashmir')
# print(indian_states)
# indian_states.extend(['Rajasthan','Goa','Andhra Pradesh'])
# print(indian_states)


##Random Selection
##1st option
# random_state = random.choice(indian_states)
# print(f"Random State : {random_state}")
# length_of_states = str(len(indian_states))
# print(f"Total no. of state : {length_of_states}")
# #2nd option
# random_index = random.randint(1,12)
# print(f"Random State is : {indian_states[random_index]}")

fruits = ['Apple','Oranges','Bananas','Pomegranate']
vegetables = ['Spinach', 'Potato','Brinjal']

mixed_items = [fruits,vegetables]   # 2D List
print(mixed_items)
print(mixed_items[1][2])    # Printing items from 2D List

