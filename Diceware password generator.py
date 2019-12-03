# Diceware password generator

import random

f = open("Diceware words.txt", "r")
words = f.readlines()
for i in range(0, len(words)):
        # Strip the line-breaks
	words[i] = words[i][:-1]
symbols = ['!','!!','"','#','##','$','$$','%','%%','&','(','( )',')','*','**','+','-',':',';','=','?','??','@']

	
def pickWord():
	# Pick a random word from the list.
	return words[random.randint(0, len(words))]

def generatePassword():
	# Create a string of 5 or 6 random words.
	password = ""
	for i in range (0, random.randint(5,6) + 1):
		password += pickWord()
		if random.randint(1, 10) != 1:
			password += " "
		else:
			password += symbols[random.randint(0, len(symbols) - 1)]
	password = password[0: len(password) - 1]
	return password

def generatePassNoSpaces():
        # Create a string of 5 or 6 random words.
        # All spaces are replaced with a symbol.
	password = ""
	for i in range (0, random.randint(5,6)):
		password += pickWord()
		password += symbols[random.randint(0, len(symbols) - 1)]
	password += pickWord()
	return password

def scrambleString(string):
	outstring = ""
	for char in string:
		if random.randint(1, 15) == 1:
			if char in ['w', 'u', 'o', 's', 'k', 'z', 'x', 'c', 'v']:
				outstring += char
			else:
				outstring += char.upper()
		else:
			outstring += char
	return outstring
	
while True:
        if (input("Enter '#' for zero-spaces: ") == "#"):
                print(scrambleString(generatePassNoSpaces()))
        else:
                print(scrambleString(generatePassword()))       
