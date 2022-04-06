"""
수들의 합
link: https://www.acmicpc.net/problem/2003
"""

import sys
si = sys.stdin.readline
N,M = list(map(int,si().split()))
N_list = list(map(int,si().split()))

R = -1
sum = 0
ans = 0
for L in range(N):
    while(R+1 < N and sum < M):
        R = R+1
        sum += N_list[R]
    if sum == M:
        ans += 1
    sum -= N_list[L]

print(ans)
