import math

def binary_search(ls, item):
    low = 0
    high = len(ls) - 1
    i = 0

    while low <= high:
        i += 1
        mid = math.floor((low + high) / 2)
        guess = ls[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    print(">>> i = ", i)
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))