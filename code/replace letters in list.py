#i want to replace letters in the list by taking multiple inputs from the user for the letters 
# to be replaced and using .replace method

from typing import List

Word_List = list(input("Enter the items for the list: ").strip().split())

print(Word_List)

#take replaced inputs
replaced_pair = []
while True:
    old_letter = input("Enter the letter you want to replace (If you done then type done at the end): ")
    if old_letter == 'done':
        break 
    new_letter = input("Enter the letter that will be replaced to the old letter: ")
    #By using double brackets, you ensure that the append() method treats the tuple as a single object 
    # and adds it as a whole to the list. Without the double brackets,each letter would be appended 
    # separately, resulting in a list of individual characters rather than pairs of letters.
    replaced_pair.append((old_letter, new_letter))

#convert list to string
word_str = ' '.join(Word_List)

#replace the input from the user
for old_letter, new_letter in replaced_pair:
    word_str = word_str.replace(old_letter, new_letter)

#convert back to list
new_list = word_str.split()

print("Modified List: ", new_list)



