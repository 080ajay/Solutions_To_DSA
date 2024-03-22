#Linhttps://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960
'''
    Time complexity: O(N)
    Space complexity: O(1)

    Where 'N' is the input array 'A'.
'''


def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Initializing the driver variables.
    small = int(1e9)
    secondSmall = int(1e9)
    large = int(-1e9)
    secondLarge = int(-1e9)

    # Iterating over an array and calculating the smaller and larger numbers.
    for i in range(n):
        small = min(small, a[i])
        large = max(large, a[i])

    # Iterating again and updating the second order numbers.
    for i in range(n):
        if (a[i] < secondSmall and a[i] != small):
            secondSmall = a[i]
        if (a[i] > secondLarge and a[i] != large):
            secondLarge = a[i]

    return [secondLarge, secondSmall]
