//link -https://www.codingninjas.com/studio/problems/reverse-bits_2181102?leftPanelTabValue=SOLUTION

#include<math.h>
long reverseBits(long n) {
    vector<int> v;

    //Finding The Binary Number of n
    while(n>0)
    {
        v.push_back(n%2);
        n=n/2;
    }

    int sz=32;
    int v_Size=v.size();
    //Appending the Zeros to given binary number
    for(int idx=1;idx<=sz-v_Size;idx++)
    {
        v.push_back(0);
    }
    long result=0;
    int temp=0;
    //Finding out the decimal Number

    for(int idx=31;idx>=0;idx--)
    {
        result=result+pow(2,idx)*v[temp];
        temp++;
    }

    return result;
}




---------------------------python-----------------------------
"""
    Time Complexity: O(1)
    Space Complexity: O(1)
"""

def reverseBits(n):
    # 'ans' will store the value of reversed bits representation.
    ans = 0

    for i in range(32):
        # 'k' is the i'th bit.
        k = n & (1<<i)

        # If the i'th bit from right is Set.
        if k>0:
            # Increase the value of ans by value of i'th bit from left.  
            ans += (1<<(31-i))
        
    return ans
