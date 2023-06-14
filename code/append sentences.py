#Write a program that takes a sentence as input from the user and 
#creates a new list where each element is a word from the sentence, reversed.

from typing import List

sentences = input("Enter your sentence: ")
words = sentences.split()
reversed_words = []

for word in words:
    reversed_word = ''.join(reversed(word))
    reversed_words.append(reversed_word)



print(reversed_words)