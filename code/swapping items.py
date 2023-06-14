#fuction for swapping last and first element of the list
def swapitems(newposition):
    size = len(newposition)
    #swap code
    temp = newposition[0]
    newposition[0] = newposition[size - 1]
    newposition[size - 1] = temp

    return newposition

#no of items
n = int(input("Enter the number of items you gonna enter: "))
#items
items = list(map(int, input("enter the numbers: ").split()))
print(items)

newposition = items

print("Items with new position")
print(swapitems(newposition))