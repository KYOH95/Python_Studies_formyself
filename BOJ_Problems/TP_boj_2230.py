#수고르기
#link: https://www.acmicpc.net/problem/2230

import sys
si = sys.stdin.readline

N,M = list(map(int,si().split()))
N_list = sorted(int(si()) for _ in range(N))

ans = 2000000000
R = 0
for L in range(N):
    while R+1 < N and N_list[R] - N_list[L] < M:
        R += 1
    if N_list[R] - N_list[L] >= M:
        ans = min(ans,N_list[R] - N_list[L])

print(ans)


