#boj_15565
#귀여운 라이언

import sys
from collections import deque
si = sys.stdin.readline

N, K = map(int,si().split())
a = list(map(int,si().split()))

R = -1
count = 0
ans = -1
for L in range(N):
    while(R+1 < N and count < K):
        R += 1
        if a[R] == 1: count += 1
    if count == K:
        if ans == -1: ans = R-L+1
        print(L,R-L+1)
        ans = min(ans, R-L+1)
        
        
    if a[L] == 1: count -= 1

print(ans)
