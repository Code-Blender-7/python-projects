# Birthday Paradox
# Author - Ahnaf Tahmid Jaheen (FoxtBird)
# Original Idea - Ai Stewgart

from datetime import datetime, timedelta
import random
## 1. Get how many birthdays to generate. Maximun range is 100

def getRange():
    while True:
        try:
            inputAmount = int(input("How many birthdays should I generate? (max 100): "))
            if inputAmount > 100:
                print("Value out of range! (max 100)")
            else: break
        except ValueError: print("Input is incorrect. Try again") 
    return inputAmount


## 2. Generate Random Dates
def generateBirthday(totalDates):
    date_list = []
    
    for date_index in range(totalDates):
        x = datetime.now() + timedelta(days=random.randint(0,365))
        date_list.append(x.strftime("%b %d"))
        
    print(date_list)
    
sample = getRange()
print(sample)

generateBirthday(sample)