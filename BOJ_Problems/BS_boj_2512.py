"""
예산
link: https://www.acmicpc.net/problem/2512

4
120 110 140 150
485
"""

import sys
si = sys.stdin.readline

N = int(si())
N_list = list(map(int,si().split()))
max_ = int(si())

def calculator():
    pass


def solution(L,R):
    ans = L-1
    while L <= R:
        mid = (L+R)//2
        if calculator():
            pass


sum = 0
for x in N_list:
    sum += x
if sum <= max_:
    print(max(N_list))
else:
    solution()

