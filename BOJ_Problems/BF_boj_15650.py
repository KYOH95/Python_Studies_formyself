"""
M과 N(2)
link: https://www.acmicpc.net/problem/15650
"""

import sys
si = sys.stdin.readline

N,M = list(map(int,si().split()))

def rec(K,N,M,selected,used):
    if K == M:
        for x in selected:
            print(x,end = " ")
        print()
    else:
        if K == 0: start = 1
        else: start = selected[K-1] + 1
        for cand in range(start,N+1):
            if used[cand] == False:
                selected[K] = cand
                used[cand] = True
                rec(K+1,N,M,selected,used)
                selected[K] = 0
                used[cand] = False

selected = [0 for _ in range(M)]
used = [False for _ in range(N+1)]
rec(0,N,M,selected,used)
            
