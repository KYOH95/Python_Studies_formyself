"""
M과N (4)
link: https://www.acmicpc.net/problem/15652
"""

import sys
si = sys.stdin.readline

N,M = list(map(int,si().split()))

def rec(K,N,M,selected):
    if K == M:
        for x in selected:
            print(x,end=" ")
        print()
    else:
        if K == 0: start = 1
        else: start = selected[K-1]
        for cand in range(start,N+1):
            selected[K] = cand
            rec(K+1,N,M,selected)

selected = [0 for _ in range(M)]
rec(0,N,M,selected)




