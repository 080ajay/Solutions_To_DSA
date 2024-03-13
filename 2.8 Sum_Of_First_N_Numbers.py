//Link -https://www.codingninjas.com/studio/problems/sum-of-first-n-numbers_8876068?leftPanelTabValue=SOLUTION
"""
    Time complexity: O(1)
    Space complexity: O(1)
"""

def sumFirstN(n: int) -> int:
    # Assign 'ans' to sum of first 'n' natural numbers.
    ans = n * (n + 1) // 2
    
    return ans

---------------------------    C++     -----------------------
long long sum_Of_Number(long long n)
{
    return (n*(n+1))/2;
}

long long sumFirstN(long long n) {

    return sum_Of_Number(n);
}

