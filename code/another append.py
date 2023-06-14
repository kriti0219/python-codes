#Write a program that takes a list of numbers as input from the user and 
# creates a new list where each element is the cumulative sum of all 
# the preceding numbers in the input list.

from typing import List

numbers = input("Enter the numbers in the list: ").split()

cumulative_sum = []
total = 0
for num in numbers:
    total +=  int(num)
    cumulative_sum.append(total)

print(cumulative_sum)


