"""
Count the branches for the following earthquake effect example:
8 (or greater)
7 to 7.99
6 to 6.99
4.5 to 5.99
Less than 4.5
"""
richter=float(input("Enter a magnitude on the richter scale :"))
if richter >= 8.0:
    print("Most structure fall")
elif richter >=7.0:
    print("Many buildings destroyed")
elif richter >=6.0:
    print("Many buildings considerable damaged, some collapse")
elif richter >=4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")