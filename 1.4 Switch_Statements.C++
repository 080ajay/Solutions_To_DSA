 //link - >https://www.codingninjas.com/studio/problems/switch-case-statement_8357244

 #include<cmath>
double areaSwitchCase(int ch, vector<double> a) {

	switch(ch)
	{
		case 1: return M_PI*a[0]*a[0];
		case 2:return  a[0]*a[1];
		
	}
}

---------------------------python-----------------------------
'''
    Time complexity: O(1)
    Space complexity: O(1)
'''

import math
from typing import *

def areaSwitchCase(ch: int, a: List[float]):
    area = 0.0

    # Using if-elif-else statements to calculate the area based on the shape.
    if ch == 1:  # Circle
        area = math.pi * a[0] * a[0]
    elif ch == 2:  # Rectangle
        area = a[0] * a[1]

    # Returning the calculated area upto 5 decimal places.
    return "{:.5f}".format(area)
