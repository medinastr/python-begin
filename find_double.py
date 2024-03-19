def find_double(l):
    for ele1 in l:
        l.remove(ele1)
        if ele1 in l:
            return ele1

    return None


l = [1, 2, 3, 3, 2, 1, 0]
print(find_double(l))
