"""
두 용액
Link: https://www.acmicpc.net/problem/2470
"""

import sys
si = sys.stdin.readline

N = int(si())
A = list(map(int,si().split()))
A.sort()

def BS(listA,L,R,X):
    while L < R:
        mid = (L+R)//2
        if listA[mid] > -X:
            R = mid-1
        elif listA[mid] <= -X:
            L = mid+1
    print(X,listA[mid])

print(A)
for i in range(1,len(A)-1):
    BS(A,i,len(A)-1,A[i-1])