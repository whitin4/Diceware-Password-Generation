# Prepare the text file

file_pdf = open("Copy from pdf of words.txt", 'r')
file_new = open("Diceware words.txt", 'w')

lines = file_pdf.readlines()
words = []
for item in lines:
	if item[0:4] == "Page":
		print('Skipping "' + item[:-1] + '"')
	elif item[0:8] == "Diceware":
		print('Skipping "' + item[:-1] + '"')
	else:
		words.append(item[6:])
		
file_new.writelines(words)
	
	
input()
