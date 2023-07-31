counter=0
s=input("Enter a text")
for i in s:
    if(i in "aeiouAEIOU"):
        counter +=1
print(counter)
