//Link -https://www.codingninjas.com/studio/problems/print-1-to-n_628290?leftPanelTabValue=SOLUTION
'''
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    where n is the integer.
'''
from typing import List

def recursiveFunction(x: int, ans: List[int]) -> None:
    if x == 0:
        return

    # Call recursive function.
    recursiveFunction(x - 1, ans)

    # Insert element in the list.
    ans.append(x)

def printNos(x: int) -> List[int]: 
    # Declaring an empty list.
    ans = []

    # Calling recursive function.
    recursiveFunction(x, ans)

    return ans


------------------------ C++ ------------------------------
#include<vector>

void print(int n,vector<int> & number,int last)
{
     number.push_back(n);
    if(n==last)
    {
        return;
    }
   
    print(++n,number,last);
}




vector<int> printNos(int x) {
    vector<int> number;
    print(1,number,x);
    return number;
}
