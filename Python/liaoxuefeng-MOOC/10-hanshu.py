# -*- coding: utf-8 -*-

import math
#二元一次方程组求解：
def quadratic(a, b, c):
    
    delta = (b**2-4*a*c)
    if delta >= 0:
        x1 = (-(b) + math.sqrt(delta))/2/a
        x2 = (-(b) - math.sqrt(delta))/2/a
        return x1,x2
    else:
        print("Don't have valid answer!\n")



#测试：
print(quadratic(2,3,1))
print(quadratic(1,3,-4))