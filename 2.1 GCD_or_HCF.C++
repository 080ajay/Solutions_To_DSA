//link-https://www.codingninjas.com/studio/problems/hcf-and-lcm_840448

int calcGCD(int n, int m){
    
    //Edge Case
    //If a number is 0 then the other number is the GCD
    if(n==0||m==0)
    {
        return n>m?n:m;
    }

    //Logic
    while(n!=m)
    {
        if(n>m)
        {
            n-=m;
        }
        else if(n<m)
        {
            m-=n;
        }
    }
    return m;

}