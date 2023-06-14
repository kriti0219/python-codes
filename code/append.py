#Write a program that takes a series of numbers as input from the user and 
#creates a new list containing only the even numbers from the input.

from typing import List

numbers = input("Enter the numbers in the list: ").split()

even_number = []

for num in numbers:
    if int(num)%2==0:
        even_number.append(int(num))

print("The even number list: ", even_number)