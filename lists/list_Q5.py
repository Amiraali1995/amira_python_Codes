"""input: [23, 54, 76, 12, 90]
output: 23 | 54 | 76 | 12 | 90
replace , coma with |
"""

mylist = [23, 54, 76, 12, 90]
replace_coma = str(mylist).replace(", ", " | ")
replace_coma=replace_coma[:-1]
replace_coma=replace_coma[1:]
print(replace_coma)




