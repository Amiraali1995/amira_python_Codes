import math
from math import sqrt
r= math.sqrt(2.0)
if r * r == 2.0:
    print("sqrt(2.0) squared is 2.0")
else:
    print("sqrt(2.0) squared is not 2.0 but ", r * r)
print("-"*60)
#use of epsilon
EPSILON= 1E-14
x1=math.sqrt(2.0)
if abs(r*r-2.0)<EPSILON:
    print("sqrt(2.0) squared is approximately 2.0")