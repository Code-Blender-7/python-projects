import random
import time

sentence = ["No", "You", "Don't", "Suck"]
random_chose = random.choice(sentence)
correct_chose = "No You Don't Suck"
complete_answer = {}
choice = []

print('check')


def case_generator():
    while True:
        choice.append(random.choice(sentence))
        choices = set(choice)
        print(choices)
        if len(choices) == 4:
            complete_answer = " ".join(choices)
            break


print(complete_answer)

while True:
    time.sleep(0.5)
    if complete_answer == correct_chose:
        print("matched - ", complete_answer)
        break
    else:
        print("failed - ", complete_answer)
        break

# while True:
#     if len(choice) != 4:
#         choice.append(random.choice(sentence))
#         print(choice)
#         break
#     if len(choice)
#         print(choice)

# while True:
# 	if len(choice) != 4:
# 	    if random_chose in choice:
# 	        pass
# 	    elif random_chose not in choice:
# 	        choice.append(random_chose)
# 	        print(choice)

# while True:
#     while

# print(" ".join(choice))
# print(len(choice))
# print(random.choice(sentence))
