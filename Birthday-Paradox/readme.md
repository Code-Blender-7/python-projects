![](https://github.com/Code-Blender-7/assets/blob/main/python-projects/Birthday-Paradox/birthday_paradox.gif)
# Introduction

Birthday Paradox is a Python analysis program where you can find the percentage of the two people having the same birthday date in the current year.


### Requirements

1. Birthday Paradox requires Python installed in your machine for it to work.

2. Birthday Paradox requires the argparse lib for it to work
Download the dependencies via the requirements.txt
```
python install -r requirements.txt
```

### Usage
This program requires a value (1 < _n_ <= 100) for generating the arrays. Follow the demo for precise instructions.

Birthday-Paradox requires an argument (dates) which is used to generate the number of dates in a single simulation.

(_test 25 birthdays in a single simulation_)
```
python main.py --dates 25
```
It also has a second optional argument (simulations) which is the number to be run over. 
(_test 25 birthdays in a single simulation over 60,000 times_)
```
python main.py --dates 25 --simulations 60000
```

#### Note 📝
Birthday Paradox runs over thousands of simulations over a random generated birthday array again and again. For performances, the default is 100,000 simulations. Please don't insert a value of arrays over 80 as it will longer time for the simulations to be completed.

### Credits
Author of code: [Black_2_white](www.twitter.com/Black_2_white)
Original Idea by Ai Stewgart

Please see his book named [_Small Book, Small Python Projects_](https://inventwithpython.com/bigbookpython/) for his own original code solution.
