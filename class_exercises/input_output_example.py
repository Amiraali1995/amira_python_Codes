##
#This program prints the price per ounce for a six-pack of cans
##
#Defines a constant for pack size

CANS_PER_PACK=6

#Obtain price per pack and can volume
user_input=input("Please enter the price for a six-pack: ")
packPrice=float(user_input)

user_input=input("Please enter the volume for each can (in ounces): ")
canVolume=float(user_input)

#Compute pack volume
packVolume=canVolume*CANS_PER_PACK

#Compute and print price per ounce
pricePerOunce=packPrice/packVolume
print("Price per ounce:%8.2f"%pricePerOunce)