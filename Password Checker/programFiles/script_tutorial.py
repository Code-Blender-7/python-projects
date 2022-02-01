# -*- coding: utf-8 -*-
# @Author: Climax
# @Date:   2022-01-30 17:12:31
# @Last Modified by:   Climax
# @Last Modified time: 2022-01-30 18:01:59



import requests
import hashlib
import sys  

# send data
def request_api_data(query_char):
	url = "https://api.pwnedpasswords.com/range/" + query_char
	responds = requests.get(url)
	
	if responds.status_code != 200:
		raise RuntimeError(f"Error. Got a {responds.status_code}. Check it again")
	return responds

# get count of hacked attempts
def get_password_leaked_count(hashes, hash_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hash_to_check:
			return count
	return 0



# check data
def pwned_api_check(password):
	# check password if exists in api
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, remain_char = sha1password[:5], sha1password[5:]
	response = request_api_data(first5_char) 
	return get_password_leaked_count(response, remain_char)


def main(password):
	count = pwned_api_check(password)
	if count:
		print(f'{password} was found matched {count}. Recommend changing it.')
	else:
		print(count)

main(input("Enter the password: "))

