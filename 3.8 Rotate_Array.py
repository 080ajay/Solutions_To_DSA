# Link- https://www.codingninjas.com/studio/problems/rotate-array_1230543?leftPanelTabValue=SOLUTION
    Time Complexity: O(n*k)
    Space Complexity: O(1)
    where n is the size of the input array.
'''

def rotateArray(arr: list, k: int) -> list:
    n = len(arr)
    for i in range(k):
        temp = arr[0]
        
        for j in range(n - 1):
            arr[j] = arr[j + 1]
            
        arr[n - 1] = temp
    return arr
