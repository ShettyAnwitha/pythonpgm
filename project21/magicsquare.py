
import numpy as np
import sys

order = int(input("Enter order of magic square: "))

if order%2==0:
    order = order+1
    print("Given order is even so it is incremented by 1.")

diagonal = order//2
magicsquare = np.zeros((order,order))

k = diagonal
j = 0

for i in range(1,order*order+1):
    magicsquare[j][k] = i
    p = j
    j = j-1
    q = k
    k = k+1
    
    
    if j<0:
        j = order-1
    
    if k>order-1:
        k = 0
    
    if magicsquare[j][k]!=0:
        k = q
        j = p+1

print("Generated Magic Square is: \n")

for j in range(order):
    print("", end="")
    
    for k in range(order):
        print("%4d " % magicsquare[j][k], end="")
    
    print()
    
    for i in range(1, 6*order+1):
        print("", end="")
    
    print()
