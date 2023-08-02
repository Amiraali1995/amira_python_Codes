



contacts={"Asma":99886655,
          "Muzun":99663322,
          "Amira":99887711,
          "Tasnim":99551122,
          "Sara":99336611,
          "Muzan":99114477}
oldContact=dict(contacts) #to create a new dictionary
print("asma number is ",contacts["Asma"])
if "Raya" in contacts:   #check if raya is in my contact
    print("Raya's number is ",contacts["Raya"])
else:
    print("Raya is not in my contacts ")
number=contacts.get("Sara",411) #instead of using if statment to check id the person is in my contacts you can you this way #411 04 404 error number that means the person is not in my contact
print("Dail "+str(number))

contacts["Sana"]=55446699 #new contact
contacts["Sana"]=99772255 #update

contacts["Sultan"]=99882244 #new contact
print(contacts)
#contacts.pop("Sultan") #to remove sultan from my contact
#temp=contacts.pop("Sultan")#if i want to remove sultan in my contact but i will use sultan again but in another case so, i have to save it in a variable

"""for key in contacts:  #print all the keys with out values 
    print(key)"""

for item in contacts.items(): #will print the key and the values of the all the contacts
    print(item[0],item[1])