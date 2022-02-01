# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-01-30 17:12:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-02-01 22:11:07

import requests
import hashlib

def sha1_generator(string):
	"""
	transform the password into sha1
	"""
	sha1password = hashlib.sha1(string.encode("utf-8")).hexdigest().upper()
	return sha1password

def api_response_data(query_char):
	"""
	get response data of the first 5 letters of the sha1 hash code.
	"""
	first5Char = sha1_generator(query_char)[:5]
	url = "https://api.pwnedpasswords.com/range/" + first5Char
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f"Error. Fetched {res.status_code}. Try again.")
	else:
		return res.text

def get_password_leaks(string):
	"""
	check the count of leaks from the response of the sha1 code.
	seperates the hash code and the count
	"""
	remainChar = sha1_generator(string)[5:] 
	hashes = (line.split(":") for line in api_response_data(string).splitlines())
	for h, count in hashes:
		if h == remainChar: # if hash code matches the remaining characters
			return count

def main(args):
	count = get_password_leaks(args)
	if count:
		print(f"Your password was found matched {count} times. Therefore it can be hacked")
	else:
		print("Your password has not found any hacking options. Therefore, your password is safe.")


while True:
	main(input("Enter your password to see if it can hacked: "))