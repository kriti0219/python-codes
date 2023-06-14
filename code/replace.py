# Write a program that takes a sentence as input and 
# replaces all occurrences of a given word with another word.

#function 
def wordreplace(sentence, wordrep, neword):
    #using .replace method
    sentence = sentence.replace(wordrep, neword)

    return sentence 

#driver function
sentence = input("Enter your sentence: ")
wordrep = input("Enter the word to be replaced: ")
neword = input("Enter the new word: ")

print("Here is your new sentence")
#function call
print(wordreplace(sentence, wordrep, neword))

