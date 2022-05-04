
#Task1: message-digest algorthms of MD5, SHA-1, SHA-256
import hashlib

def menu1():

	print("         Welcome to the hash-checker          ")
	print(" Choose the desired message-digest algorithm  ")
	print(" 1) MD5                                       ")
	print(" 2) SHA-1                                     ")
	print(" 3) SHA-256                                   ")
    
	option = input("Please enter algorithm (1, 2 or 3): ")
	phrase = input("Please enter your phrase: ")
    
	return int(option), phrase

def md5(value): #md5 algorithm 

	hash = '00000000000000000000000000000000'
	md5 = hashlib.md5() #creating an object

	md5.update( value.encode() ) #obtaining hash value
	hash = md5.hexdigest()
	return hash

def sha1(value): #sha1 algorithm 

	hash = '0000000000000000000000000000000000000000'          
	sha1 = hashlib.sha1() #creating an object

	sha1.update( value.encode()  ) #obtaining hash value
	hash = sha1.hexdigest()
	return hash

def sha256(value): #sha256 algorithm 

	hash = '0000000000000000000000000000000000000000000000000000000000000000'          
	sha256 = hashlib.sha256() #creating an object

	sha256.update( value.encode() ) #obtaining hash value
	hash = sha256.hexdigest()
	return hash

option, phrase = menu1()

if option == 1:
	hash = md5(phrase)
	print('The MD5 hash is:', hash)

elif option == 2:
	hash = sha1(phrase)
	print('The SHA1 hash is:', hash)

elif option == 3:
	hash = sha256(phrase)
	print('The SHA256 hash is:', hash)

else:
	print('Error')
