# Bagels. A Detective Logic Game
# Idea from Ai Sweigart
# Author - Ahnaf Tahmid Jaheen (FoxtBird)

import random

answer = str(random.randint(100, 999))
print(answer)


def checkList(userValue, answerValue):
    
    for i in range(3):
        if userValue[i] == answerValue[i]: print("Fermi")
        elif userValue[i] != answerValue[i]: 
            if userValue[i] in answerValue: print("Pico")
        else: 
            print("Bagels")
        
        
        
        
while True:
    user_input = input("> ")

    if user_input == answer:
        print("You got it!")
        break
    checkList(user_input, answer)