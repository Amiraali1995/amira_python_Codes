"""
calculate the avarage using file detecting
32.0
54.0
67.5
80.25
115.0

"""
# Open the file for reading
file_input = open("file_exercise.txt", "r")

# Initialize variables for sum and count of valid numbers
total_sum = 0
count = 0

# Read each line from the file
for line in file_input:
    total_sum+=float(line)
    count+=1

avg=total_sum/count
print(avg)






"""  # Strip whitespace from the line
    line = line.strip()

    # Check if the line is not empty and can be converted to a float
    if line and line.replace(".", "").isdigit():
        # Convert the line to a float and add it to the total sum
        number = float(line)
        total_sum += number
        count += 1

# Close the file
file_input.close()

# Calculate the average if there are valid numbers in the file
if count > 0:
    average = total_sum / count
    print(average)
else:
    print("No valid numbers found in the file.")
"""



