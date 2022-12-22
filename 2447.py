# 별 찍기 - 10

import sys

def printStar(n, x, y, area):
    if area == 0:
        return
    
    if x == 1 and y == 1:
        print(" ",end="")
    else:
        print("*",end="")
        
    if area%n == 1:
        x += 1
        print("")   
    if y == n-1:
        y = 0
    else:
        y += 1
    printStar(n, x, y, area-1)
        
    
n = int(sys.stdin.readline().rstrip())
printStar(n, 0, 0, n*n)