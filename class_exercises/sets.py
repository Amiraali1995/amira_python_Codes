
"""set2={}
print(type(set2))
#<class 'dict'>
""" #return the type dictionary not set because no value and set and dictionary user curley brackets

#**********************************************************************************************************

#to know the type of set the following code is
set3=set()
print(type(set3))
#<class 'set'>


#set3.add(1,2,3) error beacuse it takes only one argument

print("-"*100)
set3={"a","b","c","$$",0.25,5,True}
print(set3)
#to add more than one item we will user update method
set3.update([10,"x",False])# its unchangale unordered not duplicated
print(set3)
print("-"*100)


s1={"a","b","c"}
s2={"a","d","e","f"}

#add two sets sq and s2
print(s1.union(s2))
print("-"*100)
#print(s2.remove("c")) error
print(s1.discard("m")) #return None
print("-"*100)

s4={1,2,3,4}
print(s4.pop())
print(s4.pop())
print(s4.pop())
print(s4.pop())
#print(s4.pop()) #error because all the element no remeaning elements in side the set
print(s4) #output will be empty set b
#because we remove all the elements inside the set
print("-"*100)

#disjoint
#if there is no similarties will return true otherwise false
s5={1,2,3}
s6={4,5,6}
print(s5.isdisjoint(s6))


