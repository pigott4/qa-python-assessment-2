# reverser.py

# Ask the user for a word
word = input("Give me a word, please: ")

# Reverse the word using slicing
reversed_word = word[::-1]

print(reversed_word)

#[::-1] → is called a slice.
#The general slice pattern is [start:stop:step].
