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

---------------------------python-----------------------------
'''
    Time Complexity: O(a)
    Space Complexity: O(1)

    Where 'a' is minimum of 'n' and 'm'.
'''


def calcGDC(n: int, m: int) -> int:
    ans = 1
    # Iterating through all integers from 1 to min(n,m) and
    # finding the greatest integer that divides both 'n' and 'm'.
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            ans = i
    return ans
