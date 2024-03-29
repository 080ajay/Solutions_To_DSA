//Link-https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650

#include<iostream>
using namespace std;

int main(){

    int n;
    cin>>n;

	int evenSum = 0, oddSum = 0;

	while(n > 0) {
		int last = n % 10;
		if(last % 2 == 0) {
			evenSum += last;
		}
		else {
			oddSum += last;
		}
		n = n / 10;
	}

	cout<<evenSum<<" "<<oddSum;

}

---------------------------python-----------------------------
#main
num = int(input())

evenSum = 0 
oddSum = 0

while num > 0 :
    last = num % 10
    
    if last % 2 == 0 :
        evenSum += last
    else :
        oddSum += last
        
    num = num // 10
    
print(evenSum, " ", oddSum)
