# -*- coding: utf-8 -*-

a = (1,2,3)
b = (1,2,3)

#b = (1,[2,3])
# 执行不能,puple内部可变,无法植入set,植入set内部必须完全不可变

c = {a:213}
d = set([b])

print (c[(1,2,3)])
print (c[a])
print (c)
print (d)
