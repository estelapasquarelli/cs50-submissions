def remove_vowels(word):
    vowels = "aeiouAEIOU"
    return "".join(letter for letter in word if letter not in vowels)

word = str(input("Input: "))
print("Output: " + remove_vowels(word))
