# Link -https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278
"""
    Time complexity: O( N )
    Space complexity: O( N )

    Where 'N' is the size of array.
"""

from copy import deepcopy


def rotateArray(arr: [], n: int) -> []:

    # Create a 'copyArr' of size 'n'.
    rotatedArr = [0] * n

    # Now store ith value (1 <= i <= n-1) of 'Arr' at (i-1)th position in 'copyArr'.
    for i in range(1, n):
        rotatedArr[i - 1] = arr[i]

    # Store the 0th value of 'Arr' at (n-1)th position in 'copyArr'.
    rotatedArr[n - 1] = arr[0]

    # Return the copyArr.
    return rotatedArr

