"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730472095"

word: str = input("Enter a 5-character word: ")
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) > 5: 
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter) > 1: 
    print("Error: Character must be a singular character")
    exit()
if len(letter) < 1:
    print("Error: Character must be a singular character")
    exit()
match: int = 0
print("Searching for " +  letter  + " in " + word) 
if (letter == word [0]):
    print(letter + " found at index 0")
    match = match + 1
if (letter == word [1]):
    print(letter + " found at index 1")
    match = match + 1
if (letter == word [2]):
    print(letter + " found at index 2")
    match = match + 1
if (letter == word [3]):
    print(letter + " found at index 3")
    match = match + 1
if (letter == word [4]):
    print(letter + " found at index 4") 
    match = match + 1
if match == 0:
    print ("No instances of " + letter + " found in " + word)
else: 
    if match == 1:
        print(str(match) + " instance of " + letter + " found in " + word)
    else: 
        print(str(match) + " instances of " + letter + " found in " + word)