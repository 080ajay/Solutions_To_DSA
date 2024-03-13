//link -https://www.codingninjas.com/studio/problems/reverse-an-array_8365444
'''
    Time Complexity : O(n)
    Space Complexity : O(1)

    where n is size of input array
'''

def reverseArray(n, nums):
    # Reverse the elements in the list using the reverse() method.
    nums.reverse()

    # Return the reversed list.
    return nums

------------------------------ C++  ----------------------
#include<vector>
#include<algorithm>
vector<int> reverseArray(int n, vector<int> &nums)
{
    reverse(nums.begin(),nums.end());
    return nums;

}
