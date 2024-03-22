#Link- https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446?leftPanelTabValue=SOLUTION
from typing import *
'''
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    where n is the size of the array 'arr'.
'''

# Function to count the frequency of numbers from 1 to n in the given array 'arr'.
def countFrequency(n: int, x: int, nums: List[int]) -> int:
    freq = [0 for _ in range(n)]

    for i in range(1, n+1):
        for j in range(len(nums)):
            if nums[j] == i:
                freq[i-1] += 1
    return freq

