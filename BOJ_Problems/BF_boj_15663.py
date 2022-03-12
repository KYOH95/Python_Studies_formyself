"""
N 과 M(9)
link: https://www.acmicpc.net/problem/15663
"""

import sys
si = sys.stdin.readline
n,m = list(map(int,si().split()))
numbers = sorted(list(map(int,si().split())))
selected = [[] for _ in range(m)]
used = [False for _ in range(len(numbers))]

def rec(k):
    if k == m:
        temp = ''
        for x in selected:
            temp += str(x) + " "
        print(temp)
    else:
        lastCand = 0
        for i in range(n):
            if used[i] == False and numbers[i]!=lastCand:
                selected[k] = numbers[i]
                lastCand = numbers[i]
                used[i] = True
                rec(k+1)
                used[i] = False
                selected[k] = 0

rec(0)
