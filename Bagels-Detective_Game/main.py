# Bagels. A Detective Logic Game
# Idea from Ai Sweigart
# Author - Ahnaf Tahmid Jaheen (FoxtBird)

import random


running = True
attempts_Limit = 10
attempts = 1

def generateAnswer():
    """Creates new answer based on a new seed

    Returns:
        int: Answer of the game
    """
    random.seed(random.randint(a=1, b=100000))
    return str(random.randint(100, 999)) # Set range from 100 to 999



def bagels_intro():
    print("""
          
Welcome to the Bagels detective logic game!
Code by Ahnaf Tahmid Jaheen (FoxtBird)
Original idea by Al Sweigart al@inventwithpython.com

Here are some clues:
When I say: That means:

    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
    
I have thought up a number.
You have 10 guesses to get it.
          """)


def checkValExist(user_List, answer_list):
    """
    Checking if the given list matches the target list

    Args:
        user_List (list): User's answer in list
        answer_list (list): Correct answer in list

    Returns:
        int: How many user values int are not inside the answer list
    """
    
    NotExistValue = 0
    for i in range(3):
        if user_input[i] == answer_list[i]: print("Fermi")
        elif user_input[i] not in list(answer_list): NotExistValue += 1
        elif user_input[i] != answer_list[i]: 
            if user_input[i] in answer_list: 
                print("Pico")
                
    return NotExistValue


def continueGame():
    """
    Confirmation either the user wants to play or not.
    Mutates the running variable
    Prompts user to give an input (y/n)
    """
    global running, answer, attempts
    
    choiceContinue = input("Do you want to continue? (y/n): ")
    if choiceContinue == "y":
        attempts = 1
        print("new game!")
        answer = generateAnswer()

    elif choiceContinue == "n":
        print("Thanks for playing!")
        running = False

    else: 
        print("wrong input\nForced exit.")
        running = False



answer = generateAnswer()

bagels_intro()
while running: # main loop
    print(f"\nAttempt #{attempts}")
    user_input = input("> ")

    
    if len(str(user_input)) != 3:
        print("The Digits must be 3 characters")
        continue
    
    elif not user_input.isdigit():
        print("Strings are not allowed. Try again!")
        continue

    elif attempts == attempts_Limit and user_input != answer:
        print("Attempts Reached! Game over")
        print(f"Correct answer was {answer}\n")
        continueGame()
    
    elif user_input == answer:
        print("You got it!")
        continueGame()

    else:
        NotFoundNumbers = checkValExist(user_input, answer)
        if NotFoundNumbers == 3: print("bagels")
        attempts += 1
