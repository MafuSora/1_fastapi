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
a = 1
b = 5
fxm = 0
l = 0.001
l1 = l
i = 0

while l >= l1:

    i = i + 1
    print("Iterasi ke ", i)
    print("x1 = ", a)
    print("x2 = ", b)
    print("L = ", l)
    x11 = a
    x21 = b
    # xm f(xm)
    xm = (1/2*(a+b))
    fxm = ((xm ** 2)+(54/xm))
    print("xm = ", xm)
    print("fxm = ", fxm)

    # x1,x2
    x1 = a+(1/4*(l))
    print(x1)
    x2 = b-(1/4*(l))
    print(x2)
    a = x1
    b = x2

    # rumus
    fx1 = ((x1 ** 2)+(54/x1))
    fx2 = ((x2 ** 2)+(54/x2))
    print("fx1 = ", fx1)
    print("fx2 = ", fx2)

    # kondisi fx1
    if fx1 > fxm:
        print("fx1>fxm")

    else:
        print("fx1<fxm")

    # kondisi fx2
    if fx2 > fxm:
        print("fx2>fxm")

    else:
        print("fx2<fxm")

    if (fx1 >= fxm) and (fx2 >= fxm):
        l = (b-a)
    elif fx1 >= fxm and fx2 < fxm:
        l = (b-xm)
        a = xm
        b = x21
    elif fx1 < fxm and fx2 >= fxm:
        l = (xm-a)
        b = a
        a = x11
    elif fx1 < fxm and fx2 < fxm:
        l = l

    print(l)
    print(" ")
