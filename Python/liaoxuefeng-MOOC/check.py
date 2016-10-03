# -*- coding: utf-8 -*-

x = raw_input("Please input anything:\n")

#check for number
  #int
try:
    num = int(x)
except ValueError:
    print("Not a int Number!\n")
else:
    #print(num)
    pass
  #float
try:
    num_float = float(x)
except ValueError:
    print("Not a Number!\n")
else:
    #print(num_float)
    pass

if not isinstance(x,(int,float)):
    raise TypeError('Not Number')



#check for letters

#check for ...