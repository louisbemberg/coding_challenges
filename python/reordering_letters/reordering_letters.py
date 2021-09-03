# homework problem:
# How many letter arrangements can be made from the letters 
# - Fluke
# - Propose
# - Mississippi
# - Arrange 

# Goal: build a function that accepts a string and returns the numnber of all possible arrangements
# Optional: the function may optionally consider case sensitivity
import math

def letter_arrangements(word, case_insensitive = True):
    if case_insensitive: word = word.lower()
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    numerator = math.factorial(len(word))
    denominator = math.prod([math.factorial(i) for i in letter_count.values()])
    return int(numerator / denominator)


print(letter_arrangements("Fluke"))
print(letter_arrangements("Propose"))
print(letter_arrangements("Misssissippi"))
print(letter_arrangements("Arrange"))
print(letter_arrangements("Supercalifragilisticexpialidocious"))
