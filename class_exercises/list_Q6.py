#Write a loop that counts how many elements in a list is equal to zero

my_list = [1, 0, 5, 0, 3, 0, 7]
# Count the number of zeros in the list
zero_count = 0
for element in my_list:
    if element == 0:
        zero_count += 1
print("Number of zeros in the list:", zero_count)