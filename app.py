import json
data = json.load(open("Interactive_Dictionary_Python/data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	else:
		return "The word doesn't exist ! Please enter another word !"

word = input("Enter word : ")

print(translate(word))
