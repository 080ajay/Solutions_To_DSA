//Link -https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720

int sumOfAllDivisors(int n){
	int sum=0;
	for(int idx=1;idx<=n;idx++)
	{
		for(int j=1;j<=idx;j++)
		{
			if(idx%j==0)
			{
			sum+=j;
			}
		}
	}
	return sum;
}

---------------------------python-----------------------------
'''
    Time Complexity: O(sqrt(n))
    Space Complexity: O(1)

    Where 'n' is the given integer.
'''

def sumOfAllDivisors(n):
    ans = 0
    l = 1

    # Iterating over all values of 'l' such that 'n/l' is distinct.
    # There at most 2*sqrt(n) such values.
    while l <= n:
        val = n // l

        # 'r' = maximum value of 'i' such that 'n/i' is val.
        r = n // val
        ans += ((r * (r + 1)) // 2 - (l * (l - 1)) // 2) * val
        
        # moving on to next range.
        l = r + 1

    return ans
