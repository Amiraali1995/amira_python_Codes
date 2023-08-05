
hour1=int(input("Enter the hour for the first time : "))
minute1=int(input("Enter the minute for the first time : "))

hour2=int(input("Enter the hour for the second time : "))
minute2=int(input("Enter the minute for the second time : "))
print("-"*80)
if hour1< hour2:
    print("hour 1 comes first")
    first_hour=hour1
    first_minute=minute1
    second_hour = hour2
    second_minute = minute2
else:
    if hour1 == hour2:
        if minute1 <= minute2:
            print("hour 1 comes first")
            first_hour = hour1
            first_minute = minute1
            second_hour = hour2
            second_minute = minute2
        else:
            print("hour 2 comes first")
            first_hour = hour2
            first_minute = minute2
            second_hour = hour1
            second_minute = minute1
    else:
        print("hour 2 comes first")
        first_hour = hour2
        first_minute = minute2
        second_hour = hour1
        second_minute = minute1
#display the result
print("The first time %02d:%02d"%(first_hour,first_minute))
print("The second time %02d:%02d"%(second_hour,second_minute))
