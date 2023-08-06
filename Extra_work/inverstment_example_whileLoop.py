

RATE=5.0
INITIAL_BALANCE=10000.0
TARGET=2*INITIAL_BALANCE
balance=INITIAL_BALANCE
year=0

while balance<TARGET:
    year+=1
    interest=balance*RATE/100
    balance+=interest
print("The investment double after", year,"Years")
