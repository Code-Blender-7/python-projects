This log is dedicated to the development of the program called "password checker" explaining the process of how the whole program works from the start.


I be writing the process here in a nutshell - 

1/ takes a password as a string.
2/ Turns the string into a sha1 encoded string.
3/ send the first 5 characters of the encoded string to the API itself. 
4/ Get the response code value and gather all the data from the api generated from the encoded string. 
5/ Compare the remaining characters with the mash string that the site returned. 
6/ Return the mash code's count from the : using split and splitlines and then printing it out as the final result.

