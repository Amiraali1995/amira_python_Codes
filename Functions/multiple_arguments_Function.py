#*args syntax in Python to create a function that takes an unknown number of arguments and calculates their sum.
#In this program, the calculate_sum() function uses the *args parameter to accept any number of arguments. It then iterates over all the arguments passed to the function and adds them up to calculate the total sum. The result is returned from the function.


#When you run this program, it will print the sum of the numbers passed to the calculate_sum() function:
def calculate_sum(*args):
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum


result = calculate_sum(10,10,20,30)
print("The total sum is: ", result)
