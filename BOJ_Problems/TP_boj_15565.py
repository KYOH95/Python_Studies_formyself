"""
귀여운 라이언
link: https://www.acmicpc.net/problem/15565
"""

import sys
si = sys.stdin.readline
N,K = list(map(int,si().split()))
N_list = list(map(int,si().split()))

R = -1
ans = N+1
sum = 0
for L in range(N):
    while R+1 < N and sum < K:
        R += 1
        if N_list[R] == 1: sum += 1
    if sum >= K and R-L+1 < ans:
        ans = R-L+1
    if N_list[L] == 1:
        sum -= 1

if ans == N+1: print(-1)
else: print(ans)
