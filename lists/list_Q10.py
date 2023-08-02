# Input list of words
words = input("Enter a list of words separated by spaces: ").split()

# Get 'n' from the user
n = int(input("Enter the value of 'n': "))

# Find longer words and print the result
longer_words = [word for word in words if len(word) > n]
print("Words longer than", n, "characters:", longer_words)
