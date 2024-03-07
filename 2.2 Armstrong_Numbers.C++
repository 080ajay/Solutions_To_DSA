//Link -https://www.codingninjas.com/studio/problems/check-armstrong_589
int no_Of_Digits(int n)
{
	int count=0;
	while(n>0)
	{
		count++;
		n=n/10;
	}
	return count;
}


bool checkArmstrong(int n){

	int temp=n;
	int sum=0;
	int count=no_Of_Digits(n);
	while(n>0)
	{
		int last=n%10;
		sum=sum+pow(last,count);
		n=n/10;
	}

	return temp==sum;

}
