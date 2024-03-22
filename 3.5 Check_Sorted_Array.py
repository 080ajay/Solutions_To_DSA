#Link-https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957
'''
    Time complexity: O(N)
    Space complexity: O(1)

    Where 'N' is the input array 'A'.
'''


def isSorted(n: int,  a: [int]) -> int:
    # Iterating over the array 'A'.
    for i in range(n-1):
        if (a[i + 1] < a[i]):
            return 0

    return 1
