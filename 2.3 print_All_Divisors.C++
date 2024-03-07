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