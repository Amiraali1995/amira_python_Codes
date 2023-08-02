#When you run this program, it will prompt you to enter a string.
# After you enter the string and press Enter,
# it will print the reversed version of the input string

def reverse_string(text):
    return text[::-1]


#User input
user_input = input("Enter a string: ")
#original String input
print("Original string text",user_input)
# Reverse the input string
reversed_string = reverse_string(user_input)

# Output the reversed string
print("Reversed String:", reversed_string)
