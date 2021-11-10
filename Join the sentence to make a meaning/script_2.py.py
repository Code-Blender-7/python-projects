import random


correct_chose = "No You Don't Suck"
sentence = ["No", "You", "Don't", "Suck"]

print('check')


def case_generator():

    random.shuffle(sentence)
    return " ".join(sentence)


while True:
    if case_generator() == correct_chose:
        print("Matched", case_generator())
        break
    elif case_generator() != correct_chose:
        print("Failed", case_generator())


#         if len(choices) == 4:
#             complete_answer = " ".join(choices)
#             return complete_answer


# for i in range(5):

#     print(case_generator())

# while True:
#     if len(choice) != 4:
#         choice.append(random.choice(sentence))
#         print(choice)
#         break
#     if len(choice)
#         print(choice)

# while True:
#   if len(choice) != 4:
#       if random_chose in choice:
#           pass
#       elif random_chose not in choice:
#           choice.append(random_chose)
#           print(choice)

# while True:
#     while

# print(" ".join(choice))
# print(len(choice))
# print(random.choice(sentence))
