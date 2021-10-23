#boj_2559
#수열

import sys
si = sys.stdin.readline

N, K = map(int,si().split())
a = list(map(int,si().split()))
ans = 0
R = -1
sum = 0
for L in range(N-K):
    while R+1 < N and R-L < K-1:
        R += 1
        sum += a[R]
    
    ans = max(ans,sum)
    sum -= a[L]

print(ans)