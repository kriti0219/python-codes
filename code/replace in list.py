#Write a program that takes a list of words as input and 
# replaces all occurrences of a specific word with another word.

from typing import List

Word_List = list(input("Enter the items for the list: ").strip().split())
old_word = input("Enter the word that needs to be replaced: ")
new_word = input("Enter the new word that will replace the old word: ")

# Convert list to a string
word_str = ' '.join(Word_List)

# Perform the replacement using .replace()
modified_str = word_str.replace(old_word, new_word)

# Convert the modified string back to a list
new_list = modified_str.split()

print("Modified List: ", new_list)


'''for i in range(len(Word_List)):
    if Word_List[i] == old_word:
        Word_List[i] = new_word

print("Modified List: ", Word_List)
'''