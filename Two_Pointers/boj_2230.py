#boj_2230
#수고르기

import sys
si = sys.stdin.readline

N,M = map(int,si().split())
a = sorted(int(si()) for _ in range(N))

ans = 2000000000
R = 0
for L in range(N):
    while R+1 < N and a[R]-a[L] < M:
        R += 1

    if a[R]-a[L] >= M:
        ans = min(ans,a[R]-a[L])
    
print(ans)
