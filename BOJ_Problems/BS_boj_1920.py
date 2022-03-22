"""
수찾기
link: https://www.acmicpc.net/problem/1920
"""

import sys
si = sys.stdin.readline

N = int(si())
list_A = list(map(int,si().split()))
M = int(si())
list_B = list(map(int,si().split()))
list_A.sort()

def BS(list_,L,R,X):
    while L <= R:
        mid = (L+R)//2
        if list_[mid] == X:
            return 1
        if list_[mid] > X: R = mid-1
        else: L = mid+1
    return 0

for x in list_B:
    print(BS(list_A,0,N-1,x))




