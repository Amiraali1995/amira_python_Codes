def count_vowels(text):

    vowels = "aeiouAEIOU"
    vowel_count = 0

    for i in text:
        if i.isalpha() and i in vowels:
            vowel_count += 1

    return vowel_count

input_text = input("Enter some text: ") #example ->> HELLO PYTHON
total_vowels = count_vowels(input_text)
print("Number of vowels in the text:", total_vowels)
#OUTPUT->>>> Number of vowels in the text: 3