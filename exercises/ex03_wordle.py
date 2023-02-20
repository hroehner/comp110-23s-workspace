"""EX03 - Structured Wordle!"""

__author__ = "730472095"

def main() -> None: 
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    turns: int = 1 
    win: bool = False 
    while turns <= 6 and win == False: 
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(5)  # asks for a "5" character word 
        print(emojified(guess , SECRET))
        if guess == SECRET: 
            print(f"You won in {turns}/6 turns!") 
            return
        turns = turns + 1
    if guess != SECRET and win == False: 
        print("X/6 - Sorry, try again tomorrow! ")
        return

def contains_char(word: str, character: str) -> bool: 
    """Finding to see if character is found in index of word."""
    assert len(character) == 1  # character is length of 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == character:
            return True
        idx = idx + 1 
    else:
        return False  

def emojified(guess: str, secret: str) -> str:
    """Finding if index and/or charaacters match in guess and secret."""
    assert len(guess) == len(secret)  # make sure that length of guess is the same as length of the secret word
    idx: int = 0
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while idx < len(secret):
        if secret[idx] == guess[idx]: 
            emoji = emoji + GREEN_BOX
        if secret[idx] != guess[idx]: 
            if contains_char(secret, guess[idx]) == True:
                emoji = emoji + YELLOW_BOX
            else: 
                emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji  #  add to make sure that emoji is returned, if not None will return 

def input_guess(length: int) -> str:
    """Guess a word that is the correct length of characters, or try again."""
    attempt: str = input(f"Enter a {length} character word: ")
    while len(attempt) != length:
        attempt = input(f"That wasn't {length} chars! Try again: ")
        if len(attempt) == length:
            return attempt  # return the correct length word 
    while len(attempt) == length: 
        return attempt
   
if __name__ == "__main__":  # run to use as a module and makes it possible for toher pmodules to import functions and reuse them
    main()