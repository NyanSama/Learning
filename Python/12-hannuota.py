# -*- coding: utf-8 -*-


#汉诺塔移动函数
#表示由a借助b移动至c的N阶汉诺塔
def move(n,a,b,c):
    if n <= 0 :
        print("Disk number can't be less than 1!")
    elif n == 1 :
        print("%s --> %s" % (a,c))
    else:
        move(n-1,a,c,b)  #先移n-1阶到b
        move(1,a,b,c)    #把剩下一个大的移动到c
        move(n-1,b,a,c)  #再移n-1阶到c
        
move(5,'A','B','C')