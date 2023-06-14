from typing import List

numbers = list(map(int, input("Enter the numbers in the list: ").strip().split()))
number_find = int(input("Enter the number that needs to be checked if it exists: "))

'''if number_find in numbers:
    print("Exists")

else: 
    print("Not Exist")'''

'''for i in numbers:
    if i == number_find:
        print("True")'''

if(number_find in numbers):
    print("element exist")
else: 
    print("Element doesn't exist")

        
    
        