#remover letras específicas
def remove_vowels(word):
    vowels = "aeiouAEIOU"
    return "".join(letter for letter in word if letter not in vowels) 

#.join(): usado para juntar uma sequência de strings (como uma lista ou tupla) em uma única string, usando um separador definido

word = str(input("Input: "))
print("Output: " + remove_vowels(word))
