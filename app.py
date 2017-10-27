#imports json as dictionary
import json
#built in method to convert json to data
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[word]
    else:
        return "That word does not exist, please check your spelling"
word = input("Enter word: ")

print(translate(word))