#user input
num = int(input("Enter the number of elements in the matrix: "))
matrix_num = list(map(int, input("Enter the elements of the matrix (space-separated): ").split()))

# Count the occurrences of each element in the matrix
element_count = {}
for num in matrix_num:
    element_count[num] = element_count.get(num, 0) + 1

# Find the second most frequent element in the matrix
most_frequent_element = max(element_count, key=element_count.get)
element_count[most_frequent_element] = 0
second_most_frequent_element = max(element_count, key=element_count.get)

# Print the second most frequent element without repeating
print(f"The second most frequent element in the matrix is: {second_most_frequent_element}")
