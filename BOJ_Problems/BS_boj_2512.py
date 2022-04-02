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

def calculator(value):
    sum = 0
    for x in N_list:
        if x > value:
            sum += value
        else:
            sum += x
    return sum <= max_

def solution(L,R):
    ans = R+1
    while L <= R:
        mid = (L+R)//2
        if calculator(mid):
            L = mid + 1
            ans = mid
        else:
            R = mid -1
    return ans

print(solution(1,max(N_list)))

