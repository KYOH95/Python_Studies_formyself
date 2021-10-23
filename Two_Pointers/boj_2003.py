#boj_2003
#수들의 합2

#input: N, M
#     : 1 1 1 1

import sys
si = sys.stdin.readline

N,M = map(int,si().split())
a = list(map(int,si().split()))


R = -1
sum = 0
ans = 0
for L in range(N):
    while sum < M and R + 1 < N:
        R += 1
        sum += a[R]
        
    if sum == M: ans+=1
    sum -= a[L]

print(ans)
        