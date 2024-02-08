# I will be using the Visual Studio Code extension called Better Comments for my code.
# If you are also using VS Code I highly recommend you get the extension as well.

# For example:
# Regular Comment
# * Highlighted Comment
# ! Error Comment
# ? Question Comment
# TODO: Comment
# //Grossed Out Comment

# Join the discord: https://discord.gg/6BdusdsB

import numpy as np

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

randlist = np.random.randint(1, 100, 20)
sorted = sort(randlist)
print(randlist)
print(sorted)
help(sort)
