//Link -https://www.codingninjas.com/studio/problems/palindrome-number_624662
bool palindrome(int n)
{
    int temp=n;
    int palindrome=0;
    while(n>0)
    {
        palindrome=palindrome*10+n%10;
        n=n/10;
    }
    return palindrome==temp?1:0;
}