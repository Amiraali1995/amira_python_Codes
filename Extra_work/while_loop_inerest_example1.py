rate=5
year=0
balance=10000.0
target=20000.0
while balance< target:
    year += 1
    interest=balance*rate/100
    balance+=interest


print(year)
print("Interest:%.2f"%interest)
print("Balance: %.2f"%balance)