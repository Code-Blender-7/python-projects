This log is dedicated to the password api of the password checker.

NOTE THAT THERE COULD BE MISTAKES IN THIS LOG


The password api is the database where all the hash data is located. When you try to go to this [link](https://api.pwnedpasswords.com/range/) then you will get a invalid query. Well, it simply means that the API isn't supposed to be worked like that. From the API, add a syntax of any sentence like passwordH. When you do that, you be getting that the hash prefix is invalid or blah blah blah.

If you don't add a number to your password then you be getting that your password isn't hexadecimal. 

This api will give you a respond code of 400 which is bad. Why 400? because as said that the prefix of the hex isn't hex. The hex code is made of multiple type. The most common is called sha1 which we are using. 

The link to sha1 generator is [here](https:passwordsgenerator.net/sha1-hash-generator/).

here, any password that you will pass will become a hash code and it will be stored in the directory. 

like hello is some 15-25 words upper case letters that doesn't make sense.
to work with this api, try this code
```

import requests

user_input = "Enter your password in sha1 form: "
url = "https://api.pwnedpasswords.com/range/" + user_input
responds = requests.get(url)

if responds 


print(responds) 

```

if you get something like 400 then it isn't hash. If you get 200 then it is a variable hash line. 

so, 

<Response [200]> = Good.
<Response [400]> = It isn't a password in hash code.

remember, this api will not support your password in direct form. It will support in the first 5 characters of your password in sha1 hash. 

after you navigate to the link with your hash line, then you will see a lot or few lines with a splittext with 0 to 20.

these are the counts that are found matched with your hash/password. If the count is 0 then it means this password is new and it is hard to crack. If it is not 0 then it means that the password of yours is matched and it can be pwned which isn't good. 
