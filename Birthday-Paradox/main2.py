# Birthday Paradox
# Author - Ahnaf Tahmid Jaheen (FoxtBird)
# Original Idea - Ai Stewgart

from datetime import datetime, timedelta
from time import sleep
import random
import argparse
from argparse import RawDescriptionHelpFormatter


## 1. Get how many birthdays to generate. Maximun range is 100
def getRange():
    """
    Get the range of list to be generated.
    Updates searchLimits to mutate the values
    Returns:
        inputAmount = Number of dates per list
    """

    while True:
        try:
            inputAmount = int(input("How many birthdays should be generate? (max 100): "))
            if inputAmount > 100: print("Value out of range! (max 100)\nIf above 100 is given, it will take a long time for the calculation to be completed!\n")
            else: break
        except ValueError: print("Input is incorrect. Try again") 
    return inputAmount


## 2. Generate Random Dates
def generateBirthday(totalDates):
    """
    Function to generate birthdays

    Args:
        totalDates (int / str): Get the number of dates to be generated in a single list 

    Returns:
        list : list of birthday dates.
    """
    date_list = []

    for date_index in range(totalDates):
        x = datetime.now() + timedelta(days=random.randint(0,365))
        date_list.append(x.strftime("%b %d"))
        
    return date_list
    

# 3. Match birthdays that are the same
def matchingBirthdaysCount(birthdatesList):
    """
    Returns the matched dates count in the list
    Takes a list of dates to see if there is any occurances

    Args:
        birthdatesList (list): Birthday dates (month, day)

    Returns:
        int/str : Number of matches of each dates ones. No Duplicates
    """
    matches = []
    for i in range(len(birthdatesList)):
        if birthdatesList.count(birthdatesList[i]) > 1:
            if birthdatesList[i] not in matches:
                matches.append(birthdatesList[i])
    
    return matches


def main(searchLimits, simulationRuns=100000):
    
    simulationMatched = 0 # count of the simulation of the atttempts scenarios that had a match in them
    birthdatesMatched = 0 # Number of birthdays matched in a list
    
    print(f"Here are {searchLimits} birthdays:  \n")
    
    # EXTRA. Add Details of the upcoming simulation
    storedList = generateBirthday(searchLimits)
    print(", ".join(storedList))
    print(f"\nThere were {len(matchingBirthdaysCount(storedList))} dates that were the same")
    
    print(f"\nMatching the birthdays of {searchLimits} over {simulationRuns} times")
    if searchLimits > 80: print("Note that this may take a while") 
    
    
    # 4. Run the simulation over the specified times
    print(f"Notice. Starting the simulations over {simulationRuns} times in 3 seconds. Ctrl+C to Abort if you wish.")
    sleep(3)
    for i in range(simulationRuns):
        currentScenario = matchingBirthdaysCount(generateBirthday(searchLimits))
        if len(currentScenario) > 0: # if there is a match
            simulationMatched += 1
            birthdatesMatched += len(currentScenario)
        if i % 10000 == 0 and i != 0: print(f"Passing {i} scenario attempts. Matched: {birthdatesMatched}")
        
    print(f"""
Out of {simulationRuns} times generating over {simulationRuns*searchLimits} random dates , {birthdatesMatched} birthday dates are the same.
It means that out of {searchLimits} peoples, there is a {round(simulationMatched / simulationRuns * 100, 2)}% probability they have the same birthday.
It could be more than you think!
""")
 
# main()

parser = argparse.ArgumentParser(description="""
Birthday Paradox. A program to figure out the same birthday probability between two people.
""", 
epilog="""
Original Idea: Al Sweigart al@inventwithpython.com
Code Author: Ahnaf Tahmid Jaheen (Foxtbird)
""", 
formatter_class=RawDescriptionHelpFormatter) # Check docs of argparse. 

parser.add_argument("-d", help="Number of dates in a single simulation [required]", type=int, metavar="int")
parser.add_argument("-s", "--simulations", help="Total simulations to be run over", action="store_true")

args = parser.parse_args()

if args.d: print(args.d)
else: parser.print_help()