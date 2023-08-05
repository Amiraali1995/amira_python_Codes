price_per_Liter=1.219970
print("price per Liter %.2f"%(price_per_Liter))
print("price per Liter %10.2f"%(price_per_Liter))
#%10.2f->format specifiers
#%(price_per_Liter)-> the value to be formatted each value replace one of the format specifier in the result string
#%d The format string can contain one or more format specifier and iteral character
print("-"*100)
total=17.29547
print("total %15d"%(total))
print("%-10s%10.2f"%("total:",total)) #left justified string , two digits after the decimal point
print("-"*100)

id=24
print("%d"%(id)) #use d with integer
print("%5d"%(id)) #specifier are added so that the filed width us 5
print("%05d"%(id)) #if you add 0 before the field width 5, are added instead of spaces
print("Qutantity:%5d"%(id)) # a charcater inside a format string but outside a format specifier appear in the output
print("%d%%"%(id)) #to add a percentage sign to the output
print("-"*100)

floatig_p=1.21997
print("Floating point:%f"%(floatig_p)) #use f with floating point number
print("Floating point:%.2f"%(floatig_p)) #print two digits after the decimal point
print("Floating point:%7.2f"%(floatig_p)) #spaces are added so that the field width with 7
print("%d %10.2f"%(id,floatig_p)) #you can format multiple values at once
print("-"*100)

text="Amira"
print("%s"%(text)) #use s with string
print("%9s"%(text)) #string are right justified by defualt
print("%-9s"%(text)) #use a negstive field width to left justified


