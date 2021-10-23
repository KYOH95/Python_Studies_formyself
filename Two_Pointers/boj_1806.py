#boj_1806
#부분합

import sys
si = sys.stdin.readline

N, S = map(int,si().split())
#5 1 3 5 10 7 4 9 2 8
N_list = list(map(int,si().split()))


R, sum, ans = -1, 0, N+1
i = 0
for L in range(N):
    while R + 1 < N and sum < S:
        # i += 1
        R += 1
        sum += N_list[R]

    if sum >= S:
        ans = min(ans, R-L+1)
    
    sum -= N_list[L]
    print(L,R)

if ans == N+1: ans = 0
print(ans)
