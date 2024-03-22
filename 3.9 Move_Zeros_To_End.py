#Link - https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958
'''
    Time complexity: O(N)
    Space complexity: O(1)

    Where 'N' is the input array 'A'.
'''


def moveZeros(n: int,  a: [int]) -> [int]:
    j = 0
    # Move all the nonzero elements advance.
    for i in range(len(a)):
        if (a[i] != 0):
            a[j] = a[i]
            j += 1

    # Setting up the rest elements as a zero.
    while (j < len(a)):
        a[j] = 0
        j += 1

    return a
