# Dictionaries
# pentagonFamily = {
#     "Mustak Ahmed": "The Man Lost in the middle of Ocean",
#     "Md Sahin" : "SAP Developer at Maventic",
#     "Ariyan Chowdhury": "Software Developer at Amazon",
#     "Srijit Debsharma": "Data-Analyst at IIIM",
#     "Sajda Begam": "Entrepreneur at march"
# }
# print("\n")
# print(pentagonFamily["Mustak Ahmed"])

# Exercise
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
#
# student_grades = {}
# for key in student_scores:
#     if student_scores[key] in range(91,101):
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] in range(81,91):
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] in range(71,81):
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] in range(0,71):
#         student_grades[key] = "Fail"
# print(student_grades)

# Nesting

# tourism = {
#     "Domestic" : {"West-Bengal":["Kolkata","Burdwan",
#                                  "Darjeeling","Murshidabad"],
#                   "Karnataka":"Bangalore",
#                   "Maharastra" : "Pune",
#                   "Tamilnadu":"Chennai" },
#     "Abroad": ["Switzerland","Norway","Germany"]
# }
#
# # Printing Darjeeling
# print(tourism["Domestic"]["West-Bengal"][2])
