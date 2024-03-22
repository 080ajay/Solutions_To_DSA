#Link -https://www.codingninjas.com/studio/problems/linear-search_6922070
"""
    Time Complexity : O( N )
    Space complexity: O( 1 )

    Where N is the size of array.
"""


def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Create an ans variable and initialize with -1.
    ans = -1
    # Traverse the vector.
    for idx in range(n):
        # If nm is present.
        if arr[idx] == num:
            # update ans.
            ans = idx
            break
    # return.
    return ans
