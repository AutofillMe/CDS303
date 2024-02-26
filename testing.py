import numpy as np
import time

def sort(list):
    """
    Quicksort recursive algorithm

    Input: list (min len = 0, max len = n)

    Output: list (len = n)
    """
    if len(list) <= 1:
        return list

    randomPivot = list[0]
    pivot = [i for i in list if i == randomPivot]
    left = [i for i in list if i < randomPivot]
    right = [i for i in list if i > randomPivot]

    list = sort(left) + pivot + sort(right)
    return list

randlist = np.random.randint(1, 100, 2000)
start = time.perf_counter()
sorted = sort(randlist)
end =  time.perf_counter()
duration = end - start
print(f"Quicksort took {duration:.4f} seconds.")
print(randlist[:20])
print(sorted[:20])
help(sort)
