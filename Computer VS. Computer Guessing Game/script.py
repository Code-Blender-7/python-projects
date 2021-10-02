import random

__version__ = 3.9.6


# 1. Generate Answer Value from Range of 1 to 10
guess_no = random.randint(a=1, b=10)
attempts = 0
while True:
    # 2. Generate random Number based on Random Seed (1 <= x <= 100000)
    random.seed(random.randint(a=1, b=100000))
    choice = random.randint(a=1, b=10)

    if choice <= 10:
        if choice == guess_no:
            attempts += 1 
            print(f'Machine got it correct at attempt {attempts}')
            break
        else:
            # 3. failure Attempt count
            attempts += 1 
            print(f'Attempt#{attempts} failed')
            continue
