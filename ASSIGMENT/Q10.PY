10. Search and Match Functions

Theory:
    
• Using re.search() and re.match() functions in Python’s re module for pattern
matching.

Python’s re module provides powerful tools for working with regular expressions,
which are patterns used to match sequences of characters in strings.

1. re.match()

This function checks for a match only at the beginning of the string.
Returns a match object if the pattern is found at the start; otherwise, returns None.

import re
text = "Python is fun"
match = re.match("Python", text)
if match:
    print("Match found at the beginning")
else:
    print("No match")

2. re.search()

This function searches the entire string for the first location where the pattern matches.
Returns a match object if found anywhere in the string.

import re
text = "Learning Python is fun"
search = re.search("Python", text)
if search:
    print("Match found somewhere in the string")
else:
    print("No match")


• Difference between search and match.

re.match()                                      re.search()
Checks only at the beginning of the string	Searches throughout the entire string
Use when you expect the pattern at the start	Use when the pattern can occur anywhere
Match object if pattern is at start, else None	Match object if pattern is found, else None
Slightly faster if pattern is expected at start	May take more time if searching long strings



Lab:
    
• Write a Python program to search for a word in a string using re.search().

import re


text = "Python is a powerful programming language"
word = "powerful"


match = re.search(rf"\b{word}\b", text)


if match:
    print(f"The word '{word}' was found in the string.")
else:
    print(f"The word '{word}' was NOT found in the string.")


• Write a Python program to match a word in a string using re.match().

import re


text = "Python is a versatile language"
word = "Python"


match = re.match(rf"\b{word}\b", text)


if match:
    print(f"The word '{word}' is at the beginning of the string.")
else:
    print(f"The word '{word}' is NOT at the beginning of the string.")


Practical Examples:
23) Write a Python program to search for a word in a string using re.search().

import re


text = "Artificial Intelligence is the future of technology."


word = "future"


match = re.search(rf"\b{word}\b", text)


if match:
    print(f"The word '{word}' was found in the string.")
else:
    print(f"The word '{word}' was NOT found in the string.")



24) Write a Python program to match a word in a string using re.match().

import re


text = "Machine learning is interesting."


word = "Machine"


match = re.match(rf"\b{word}\b", text)


if match:
    print(f"The word '{word}' is at the beginning of the string.")
else:
    print(f"The word '{word}' is NOT at the beginning of the string.")

