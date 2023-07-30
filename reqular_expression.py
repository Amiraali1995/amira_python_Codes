import re
regex_patterns=r'\(\+\d{3}\)\d{4}-\d{4}$'

#user input
phone_num=input("Enter your phone number")
if re.match(regex_patterns,phone_num):
    print("valid phone number")
else:
    print("invalid phone number")