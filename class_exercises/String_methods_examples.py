#string method=
# 1.upper(), lower()
"""
2.replace()->method can take maximum of 3 parameters:
old
new
count(optional)
"""


#
# , lower(), replace(), find(), rfind
title="pythoon for everyone"
print("replace(), upper(), lower() methods")
title1="PYTHON FOR EVERYTHING"
print(title[0])
print("-"*70)
print(title.replace("for everyone","****"))
print("-"*70)
print(title.upper())
print("-"*70)
print(title1.lower())
print("-"*70)
print(title.replace("for everyone","program"))
print("-"*70)
print("-"*70)
#*************************************************************
quote="Let it be, let it be, let it be"
result1=quote.replace("let it","not")
print(result1)
print("-"*70)
result2=quote.replace("let it","not",1)
print(result2)
print("-"*70)
#find(()
"""
The find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1
The find() method takes maximum of three parameters:
The syntax of find method is 
s.find(substring)   or   s.find(substring, start)   or s.find(substring, start, end) :
"""
print("Find method")
resultf1=quote.find('let it be')
print(resultf1)

resultf2=quote.find('small')
print(resultf2)

resultf3=quote.find('let it be',12)
print(resultf3)
print("-"*70)

"""
The rfind() returns the index of most rightmost matched substring of the string. It returns -1 if substring not found.
The rfind() method takes maximum of three parameters:
The syntax of rfind method is 
s.rfind(substring)   or   s.rfind(substring, start)   or s.rfind(substring, start, end) :
"""
#rfind()
print("rFind method")
resultrf1=quote.rfind('let it be')
resultrf2=quote.rfind('small')
resultrf3=quote.rfind('let it be',12)
print(resultrf1)
print(resultrf2)
print(resultrf3)