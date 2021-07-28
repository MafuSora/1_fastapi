#!/bin/python

import math
import os
import random
import re
import sys


# if __name__ == '__main__':
#     list_weirdo=[3]
#     n = int(raw_input().strip())
#     for i in range (6,21):
#         list_weirdo.append (i)

#     if n in list_weirdo :
#         print("Weird")
#     else :
#         print("Not Weird")

if __name__ == '__main__':
    n = int(raw_input().strip())
    if 2 <= n <= 5 and n % 2 != 0:
        print("Weird")
    elif 6 <= n <= 20 and n % 2 == 0:
        print("Weird")
    elif n > 20 and n % 2 != 0:
        print("Weird")
    else:
        print("Not Weird")
