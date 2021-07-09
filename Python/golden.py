# -------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Acer
#
# Created:     02/11/2020
# Copyright:   (c) Acer 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------


# A.
"""
a= int(input("A"))
b= int(input("B"))
l= float(input("L"))
"""
a = 0
b = 5
r = 0.61803

fxm = 0
l = 0.001
l1 = l
i = 0
d = 0
while l >= d:

    i = i + 1
    print("Iterasi ke ", i)
    print("x1 = ", a)
    print("x2 = ", b)
    print("L = ", l)
    x11 = a
    x21 = b

    d = r*(b-a)

    # x1,x2
    x1 = r+a
    print(x1)
    x2 = r-b
    print(x2)
    a = x1
    b = x2

    # rumus
    fx1 = ((x1 ** 2)+(54/x1))
    fx2 = ((x2 ** 2)+(54/x2))
    print("fx1 = ", fx1)
    print("fx2 = ", fx2)

    # kondisi fx1
    if fx1 > fx2:
        print("fx1>fx2")
        b = a
        a = x11

    else:
        print("fx1<fx2")
        a = b
        b = x21

    print(" ")
