"""Guess That Number Game."""

__author__ = "730472095"

import random 

points: int = 0
player: str = ""
SMILE: str = "\U0001F600"
HEART_EYES: str = "\U0001F60D"


def main() -> None: 
    """Entrypoint of the game."""
    greet() 
    global points
    choice = input(f"Hi {player}! You have 3 choices of how you would like to proceed with the game. Your choices are: 1.Guess a number between 1 and 5 correctly in three tries for a point, 2.Guess a number between 1 and 2 three times in a row for points, or 3.Exit the game. ")
    while choice != "3": 
        if choice == "1": 
            guess: int = int(input("Guess a number between 1 and 5: "))
            answer = random.randint(1, 5)
            points = guess_the_number(guess, answer)
            print(f"You have {points} points! ")
        elif choice == "2":
            two_in_a_row_game()
        choice = input(f"Hi {player}! You have 3 choices of how you would like to proceed with the game. Your choices are: 1.Guess a number correctly in three tries for a point, 2.Guess a number between 1 and 2 three times in a row for points, or 3.Exit the game. ")
    if choice == "3": 
        print(f"You have a total of {points} points. Come back and play soon!")
        return 
    

def guess_the_number(guess: int, answer: int) -> int:  
    """Guess the number starting with 5 points and losing one with each incorrect guess!"""
    points: int = 0
    playing: bool = True
    while playing: 
        if guess == answer:
            print(f"Correct! You guessed the right answer {SMILE}! ")
            playing = False
            points += 1
        else: 
            guess = int(input("Not quite. Guess again: "))
            # print("Wrong guess. Try again! ")
            points -= 1 
    return points


def two_in_a_row_game() -> None: 
    """Choose a number between 1 and 2 and try and guess twice in a row correctly."""
    points = 0 
    shuffle = random.randint(1, 2)
    while points < 2:
        guess: int = int(input(f"Hello {player}, to win you must guess 2 consecutive times correctly. Choose a number between 1 and 2. "))
        shuffle = random.randint(1, 2)
        if guess == shuffle: 
            print(f"Right! The random number was {shuffle}. ")
            points += 1 
            print(f"You now have {points} points.")
            shuffle = random.randint(1, 2)
        else: 
            points = 0 
            print(f"Not quite. The number was {shuffle}. You are back to {points} points.")
    print(f"Success! You have won the game and earned {points} points {HEART_EYES}! ")


def greet() -> None:
    """Welcome statement!"""
    print("Hello! Welcome to Guess that Number! ")
    global player
    player = input("What is your name? ")
     

if __name__ == "__main__": 
    main()