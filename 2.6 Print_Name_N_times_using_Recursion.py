//link -https://www.codingninjas.com/studio/problems/print-1-to-n_628290?leftPanelTabValue=SOLUTION
"""
    Time Complexity: O(n)
    Space Complexity: O(n)

    Where 'n' is the given integer.
"""

def printNtimes(n: int) -> None:
    print("Coding Ninjas ", end="")

    # Recursively calling printNtimes as long as 'n' > 1.
    if n > 1:
        printNtimes(n - 1)
      
---------------------------  C++ -----------------------------

#include<vector>
vector<string> result;

void recursion(int x)
{
	if(x==1)
	{
		result.push_back("Coding Ninjas");
		return;
	}
	recursion(--x);
	result.push_back("Coding Ninjas");
	return;
}




vector<string> printNTimes(int n) {
	recursion(n);
	return result;
	
}
