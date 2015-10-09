# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']

print("===Using for===")
for name in L:
    print("Hello,%s!" % name)
print("===Using while===")
i = 0
while i < len(L):
    print("Hello,%s!" % L[i])
    i += 1
