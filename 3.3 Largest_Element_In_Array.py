#Link-https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
"""
    Time complexity: O( N )
    Space complexity: O( 1 )

    Where 'N' is the size of array.
"""


def largestElement(arr: [], n: int) -> int:

    # Create a temporary variable 'maxElement' and initialize it with 0.
    maxElement = 0

    # Traverse the array.
    for i in arr:

        # Update maxElement with the max of the current element of arr or maxElement.
        maxElement = max(maxElement, i)

    # Return 'maxElement'.
    return maxElement
