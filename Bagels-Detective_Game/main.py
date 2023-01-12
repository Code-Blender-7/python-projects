# Bagels. A Detective Logic Game
# Idea from Ai Sweigart
# Author - Ahnaf Tahmid Jaheen (FoxtBird)

import random

answer = str(random.randint(100, 999))
print(answer)
    
def checkValExist(user_List, answer_list):
    NotExistValue = 0
    for i in range(3):
        if user_input[i] == answer[i]: print("Fermi")
        elif user_input[i] not in list(answer): NotExistValue += 1
        elif user_input[i] != answer[i]: 
            if user_input[i] in answer: 
                print("Pico")
    return NotExistValue
                
while True:
    user_input = input("> ")

    if len(list(user_input)) > 3:
        print("More than 3 chars are not allowed")
        continue

    elif user_input == answer:
        print("You got it!")
        break
    
    else:
        print(checkValExist(list(user_input), list(answer)))
        
