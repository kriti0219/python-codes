#swap function 
def swapelements(elements, pos1, pos2):
    #using .pop method
    element1 = elements.pop(pos1)
    element2 = elements.pop(pos2-1)

    #inserting the elements back using .insert method
    elements.insert(pos1, element2)
    elements.insert(pos2, element1)

    return elements

#driver code
n = int(input("Number of items in list: "))

elements = list(map(int, input("enter the items: ").strip().split()))
pos1 = int(input("enter the postion 1: "))
pos2 = int(input("enter the postion 2: "))
# function call
print(swapelements(elements, pos1-1, pos2-1))