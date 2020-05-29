import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input(""))
    m = bin(n).lstrip('0b')
    maxcount=0
    for i in range(len(m)):
        if m[i]=="1":
            count=1
            for j in range(i+1,len(m)):
                if m[j]=="1":
                    count+=1
                    continue
                break
            if count>maxcount:
                maxcount=count
    print(maxcount)
