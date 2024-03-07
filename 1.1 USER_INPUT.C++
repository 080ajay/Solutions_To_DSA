//Link to Question - https://www.codingninjas.com/studio/problems/find-character-case_58513
#include<stdio.h>

int main(){

    char ch;
    scanf("%c",&ch);

    int ans;
    if(ch >= 'A' && ch <= 'Z'){
        ans = 1;
    }else if(ch >= 'a' && ch <= 'z'){
        ans = 0;
    }else{
        ans = -1;
    }

    printf("%d",ans);

}
