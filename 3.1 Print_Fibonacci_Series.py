//link -https://www.codingninjas.com/studio/problems/print-fibonacci-series_7421617?leftPanelTabValue=SOLUTION
'''
    Function to print the first n Fibonacci numbers.

    Time Complexity: O(n)
    Space Complexity: O(n)
'''
from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Create a list to store the Fibonacci numbers.
    fib = [0, 1]  

    # Generate the Fibonacci numbers.
    for i in range(2, n):

        # Compute the next Fibonacci number.
        fib.append(fib[i - 1] + fib[i - 2])  

    return fib[:n]

                -------------------  C++  ----------------------

#include<vector>

void recursion(int idx,vector<int> &result,int n)
{
    if(idx==n)
    {
        return;
    }
    result.push_back(result[idx-1]+result[idx-2]);
    idx++;
    recursion(idx,result,n);
    return;
}

vector<int> generateFibonacciNumbers(int n) {

    //Declaration
    vector<int> fibonacci;

    if(n==1)
    {
        return {0};
    }
    else if(n==2)
    {
        return {0,1};
    }

    fibonacci.push_back(0);
    fibonacci.push_back(1);    

    recursion(2,fibonacci,n);
    
    return fibonacci;



}
