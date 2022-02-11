## Program Description -

**Password Checker** is a python program that can act as a validator to use if your password is crackable or not. This is a command-line program so there is no GUI here. 
I got this project from the tutorial done by Andrei Neagoie who is a talented developer in python. Would recommend that you check out his twitter in the Credits section. 


## How The Program Works -

There are 2 program files related to this project. These includes - 
1. script_original.py
2. script_tutorail.py

I be explaining the script_original here.

The program uses the *haveibeenpwned* api to extract the sha1 hash code from the database. Then it turns your password into a sha1 hash code and then checks for matches. If there is a match found then.... you better change your password otherwise you can carry on.

To do that the first step was to create a fucntion that can request the data from the api itself. Of course, there isn't any delay or waiting time for accessing the api since it is free for all.

Afterwards, it takes your input of a password and then converts it into a sha1 code. For that reason, it uses a python built-in lib called hashlib. There are a lot of hash features here so I recommend that you check it out if you are developing any project related to hashes.

To communicate with the api, the second function takes the first 5 characters of the hash code and then it simply search it into the api database. If the first 5 char are invalid then it will respond with an error code 400 which is not good.

Afterwards, the 3rd function is to match the remaining characters excluding the 5 characters with the api database.
The datalines over the api include a : sign that separates the mash code and the count. If the count is more than 0 then... you have been pwned.

### STRUCTURE OF THE PROJECT
![image](https://github.com/Code-Blender-7/Learning-Python/blob/main/Password%20Checker/Images_for_readme/structure.png?raw=true)

#### Download the program files using [Downgit](https://minhaskamal.github.io/DownGit/#/home?url=https:%2F%2Fgithub.com%2FCode-Blender-7%2FLearning-Python%2Ftree%2Fmain%2FPassword%20Checker%2FprogramFiles)

### Credits -

Original developer - [@Black_2_white](https://twitter.com/Black_2_white)

Tutorial Developer - [@AndreiNeagoie](https://twitter.com/andreineagoie)


