import json
from difflib import get_close_matches

data = json.load(open("Interactive_Dictionary_Python/data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead ? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
		if yn is "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn is "N":
			return "The word doesn't exist ! Please enter another word !"
		else:
			return "We didn't understand your entry."
	else:
		return "The word doesn't exist ! Please enter another word !"

word = input("Enter word : ")

output = translate(word)

if type(output) is list:
	for item in output:
		print(item)
else:
	print(output)
	
