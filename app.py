#imports json as dictionary
import json

#will determine how close a word is to matching the keys in the database, returns a ratio of matching
from difflib import get_close_matches

#built in method to convert json to data
data = json.load(open("data.json"))

#main function that takes w as input from user
def translate(w):
    
#standard error message
    error = "There was an error, please try again"
    
#converts input to lower case to avoid capitalization confusion
    w = w.lower()
    
# if there is a match, return the definition
    if w in data:
        return data[w]
        
#if first conditional evals false, check for second conditional to see if get_close_matches can find anything (array size is greater than 0)
    elif len(get_close_matches(w, data.keys())) > 0:
        
#retrieves closest match and displays in uppercase for readability, expects users input of " " (return), y, or Y
        answer = input("did you mean %s instead? Y/n " % get_close_matches(w, data.keys())[0].upper())
        
#if user answers yes, return definition of closest match word
        answer.lower()
        if (answer == "" or answer == "y" or answer =="yes"):
            return data[get_close_matches(w, data.keys())[0]]    
       
        elif (answer == "n" or answer == "no"):
            
            return error
            
#if user does not enter "y, Y, yes, n, N, or no" return error message     
        else:
            return error
#if word has no match
    else:
            return error
            
#main input from user    
word = input("Enter word: ")

#calls translate function with user input as argument
output = (translate(word))

#iterate through output list to beautify returned definitions
if type(output) == list:
    for item in output:
        print(item)
  else: 
      print(output)