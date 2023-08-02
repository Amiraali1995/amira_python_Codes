#from the given dictionary write code to print the name of people who are above 22 years old

dec={1 : {'name':'John','age':27,'sex':'Male'},
     2 : {'name':'Marie','age':22,'sex':'Female'},
     3 : {'name':'Sail','age':23,'sex':'Female'}}
#sort the dictionary by age

"""#print age names that is above 22
for key, item in dec.items():
    if item['age'] > 22:
        print(item['name'])"""



def get_age(item):
    return item[1]['age']

# Sort the dictionary by age
sorted_dec = dict(sorted(dec.items(), key=get_age))

print(sorted_dec)





