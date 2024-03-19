"""
find_first_duplicate(l) will receive a list of numbers, that will return -1 if are no
duplicate numbers or the first duplicate number in list.
The first duplicate is considered the second number that appears first.
"""

def find_first_duplicate(l):

    smaller_index = len(l)
    intact_list = l.copy()
    found_numbers = []

    for ele1 in l:
        lista_aux = l.copy()
        lista_aux.remove(ele1)

        if ele1 in lista_aux:
            i = lista_aux.index(ele1)

            if i < smaller_index and ele1 not in found_numbers :
                smaller_index = i
            found_numbers.append(ele1)
    
    if smaller_index == len(l) :
        return -1
    return intact_list[smaller_index + 1]


l = [1, 3, 2, 10, 2, 3, 0]
print(find_first_duplicate(l))
