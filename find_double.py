"""
find_first_duplicate(l) will receive a list of numbers, that will return -1 if are no
duplicate numbers or the first duplicate number in list.
The first duplicate is considered the second number that appears first.
"""

def find_first_duplicate(l):
    first_duplicate = -1
    found_numbers = set()

    for ele1 in l:
        if ele1 in found_numbers :  # check if it is a duplicate number in list
            first_duplicate = ele1
            break

        found_numbers.add(ele1)

    return first_duplicate


l = [1, 3, 2, 10, 2, 3, 0]
print(find_first_duplicate(l))
