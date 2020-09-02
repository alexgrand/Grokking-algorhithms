def quick_sort(arr):
    global iterations
    iterations += 1
    print(iterations)

    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(0)
        less = [i for i in arr[:] if i <= pivot]
        greater = [i for i in arr[:] if i > pivot]

        extended_arr = quick_sort(less) + [pivot] + quick_sort(greater)

        return extended_arr


arr = [33, 15, 10, 121, 17, 4, 0, 13]

iterations = 0
print(quick_sort(arr))
