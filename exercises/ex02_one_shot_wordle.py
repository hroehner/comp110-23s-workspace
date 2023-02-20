"""EX02 - One Shot Wordle - Loops."""

__author__ = "730472095"

SECRET: str = "python" 
guess: str = input("What is your 6-letter guess? ")
playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
emoji: str = ""
exists: bool = False
alternate_idx: int = 0

while len(guess) != len(SECRET):
    guess = input("That was not 6 letters! Try again: ")
while idx < len(SECRET):  # finding to see if index matches
    if SECRET[idx] == guess[idx]: 
        emoji = emoji + GREEN_BOX
    if SECRET[idx] != guess[idx]: 
        while alternate_idx < len(SECRET):  # letter in guess not same index
            if SECRET[alternate_idx] == guess[idx]:
                exists = True
            alternate_idx = alternate_idx + 1
        if exists:
            emoji = emoji + YELLOW_BOX
        else: 
            emoji = emoji + WHITE_BOX
    exists = False  # add this line to make sure it stops
    alternate_idx = 0
    idx = idx + 1
print(emoji)

if guess == SECRET:
    print("Woo! You got it! ")
else: 
    print("Not quite. Play again soon")
    playing = False
        