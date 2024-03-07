//Link -https://www.codingninjas.com/studio/problems/check-prime_624934

 #include<cmath>

bool isPrime(int n)
{
	if(n==1) return false;

	for(int idx=2;idx<=sqrt(n);idx++)
	{
		if(n%idx==0)
		{
			return false;
		}
	}
	return true;
}
