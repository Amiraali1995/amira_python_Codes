country=input("Enter the country: ")
state=input("Enter the state or province: ")

shippingCost=0.0

if country == 'USA':
    if state == "AK" or state=='HI':
        shippingCost=10.0
    else:
        shippingCost=5.0
else:
    shippingCost=10.0
print("Shipping cost to %s,%s:%.2f" % (state,country,shippingCost))