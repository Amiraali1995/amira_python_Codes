
#compute the discount for a given purchase

#obtain the original price
originalPrice=float(input("Enter the original price before the discount :"))
#Determind the discount rate
if originalPrice <128:
    discountRate=0.98
else:
    discountRate=0.84
discountedPrice = discountRate*originalPrice
print("Discounted price : %.2f" % discountedPrice)