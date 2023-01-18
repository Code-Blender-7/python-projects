# Birthday Paradox
# Author - Ahnaf Tahmid Jaheen (FoxtBird)
# Original Idea - Ai Stewgart

from datetime import datetime, timedelta
import random

searchLimits = 0
birthdatesMatched = 0
scanTrials = 100000


## 1. Get how many birthdays to generate. Maximun range is 100
def getRange():
    global searchLimits
    while True:
        try:
            inputAmount = int(input("How many birthdays should be generate? (max 100): "))
            if inputAmount > 100: print("Value out of range! (max 100)\nIf above 100 is given, it will take a long time for the calculation to be completed!\n")
            else: break
        except ValueError: print("Input is incorrect. Try again") 
    searchLimits = inputAmount


## 2. Generate Random Dates
def generateBirthday(totalDates):
    date_list = []

    for date_index in range(totalDates):
        x = datetime.now() + timedelta(days=random.randint(0,365))
        date_list.append(x.strftime("%b %d"))
        
    return date_list
    

# 3. Match birthdays that are the same
def getMatchingBirthdays(birthdatesList):
    global birthdatesMatched
    for i in range(len(birthdatesList)):
        if birthdatesList.count(birthdatesList[i]) > 1: 
            birthdatesMatched += 1
            return True
        
def main():
    simulationMatched = 0
    print("""
Birthday Paradox. A program to figure out the same birthday probability between two people.
Original Project Idea by Al Sweigart al@inventwithpython.com
Code Author: Ahnaf Tahmid Jaheen (Foxtbird)
    """)
    getRange()
    print(f"Here are {searchLimits} birthdays:  \n")
    storedList = generateBirthday(searchLimits)
    print(", ".join(storedList))
    getMatchingBirthdays(storedList)
    if birthdatesMatched > 0: print(f"\nHere {birthdatesMatched} people have their birthdays matched\n")
    elif birthdatesMatched == 0: print("\nHere, there is no people who have same birthdays. Possibly due to low people dates.\n")
    
    print(f"Matching the birthdays of {searchLimits} over {scanTrials} times")
    if searchLimits > 80: print("Note that this may take a while") 
    
    input("Enter anything to start the matching sequence: \n")
    for i in range(scanTrials):
        if getMatchingBirthdays(generateBirthday(searchLimits)) == True: simulationMatched += 1
        if i % 10000 == 0 and i != 0: print(f"Passing {i} scenario attempts. Matched: {birthdatesMatched}")
        
    print(f"""
Out of {scanTrials} times generating over {scanTrials*searchLimits} random dates , {birthdatesMatched} birthday dates are the same.
It means that out of {searchLimits} peoples, there is a {round(simulationMatched / scanTrials * 100, 2)}% probability they have the same birthday.
It could be more than you think!
""")


main()

