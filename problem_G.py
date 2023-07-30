"""""
Final exams are approaching, and Sarah wants to prepare well for them. Sarah studies n number of subjects in school, and she needs
X number of days to study each subject. Sarah plans to finish studying all the subjects before the first exam begins
final, which will be due after a number of y days. Can Sarah achieve her goal and finish studying all the subjects before
The beginning of the first exam?

"""

num_of_subjects = int(input("Enter number of subjects: "))
num_of_days = int(input("Enter number of needed days: "))
num_of_days_left = int(input("Enter number of days left for the first exam: "))
if(num_of_subjects*num_of_days<=num_of_days_left):
    print("Pass")
else:
    print("Fail")