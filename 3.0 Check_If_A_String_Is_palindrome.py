//link -https://www.codingninjas.com/studio/problems/check-palindrome-recursive_624386?leftPanelTabValue=SUBMISSION
'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is the length of the string
'''

def isPalindrome(string: str) -> bool:
    size=len(string)
    # Base case: If the length of string is 1, the string is a palindrome.
    if size <= 1:
        return True
    # If the characters at the left and right pointers are not equal, the string is not a palindrome.
    if string[0]!=string[size-1]:
        return False
    # Recurse for the substring by moving the left pointer to the right and the right pointer to the left.
    return isPalindrome(string[1:-1])


----------------------  C++  ---------------
void isPalindrome(int start,int end,string &s)
{
    if(start>end)
    {
        return;
    }
    swap(s[start],s[end]);
    return isPalindrome(start+1,end-1,s);
}




bool isPalindrome(string& s) {
    string palindrome_String=s;
    isPalindrome(0,s.size()-1,s);
    return palindrome_String==s;
}
