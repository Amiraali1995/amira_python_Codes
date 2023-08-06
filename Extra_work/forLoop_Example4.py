RATE=5.0
INITIAL_BALANCE=10000.0
numYears=int(input("Enter number of years: "))
balance=INITIAL_BALANCE
for year in range(1,numYears+1):
    instance=balance*RATE/100
    balance=balance+instance
    print("%4d%10.2f"%(year,balance))
"""
output:
Enter number of years: 10
   1  10500.00
   2  11025.00
   3  11576.25
   4  12155.06
   5  12762.82
   6  13400.96
   7  14071.00
   8  14774.55
   9  15513.28
  10  16288.95
"""