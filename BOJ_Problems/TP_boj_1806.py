"""
부분합
link: https://www.acmicpc.net/problem/1806
"""

import sys
si = sys.stdin.readline

N, S = list(map(int,si().split()))
N_list = list(map(int,si().split()))

ans = N+1
R = -1
sum = 0

for L in range(N):
    while R+1<N and sum < S:
        R += 1
        sum += N_list[R]
    if sum >= S:
        ans = min(ans,R-L+1)
    sum -= N_list[L]

if ans == N+1:
    print(0)
else:
    print(ans)




# #2중 for문
# def cal(start):
#     sum = 0
#     for i in range(start,N):
#         sum += N_list[i]
#         if sum >= S:
#             return i-start+1
#     return N+1

# for i in range(N):
#     if cal(i) < ans:
#         ans = cal(i)

# if ans == N+1:
#     print(0)
# else:
#     print(ans)