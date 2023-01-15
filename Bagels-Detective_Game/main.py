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
        user_List (list): User's answer in list (str)
        answer_list (list): Correct answer in list (str)

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

    # 1. detect if the value has a string letter on it
    if not user_input.isdigit():
        print("Strings are not allowed. Try again!")
        continue
    
    # 2. detect if the value is exceeded or below parameters
    elif not int(user_input) >= 100 or int(user_input) > 999:
        print("Given answer is invalid to conditions")
        continue
    
    # 3. Check if attempts are reached and answer is still not correct
    elif attempts == attempts_Limit and user_input != answer:
        print("Attempts Reached! Game over")
        print(f"Correct answer was {answer}\n")
        continueGame()
        
    # 4. Check if answer is a match (correct answer)
    elif user_input == answer:
        print("You got it!")
        continueGame()

    # 5. If none of the above, return the clue to the player (fermi, pico, bagels)
    else:
        NotFoundNumbers = checkValExist(user_input, answer)
        if NotFoundNumbers == 3: print("bagels")
        attempts += 1
