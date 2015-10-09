# -*- coding: utf-8 -*-

x = raw_input("Please input anything:\n")

#check for number
  #int
try:
    num = int(x)
except ValueError:
    print("Not a int Number!\n")
else:
    print(num)
  #float
try:
    num_float = float(x)
except ValueError:
    print("Not a Number!\n")
else:
    print(num_float)

#check for letters

#check for ...