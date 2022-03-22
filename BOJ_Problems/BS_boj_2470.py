"""
두 용액
Link: https://www.acmicpc.net/problem/2470
"""

import sys
si = sys.stdin.readline
N = int(si())
A = list(map(int,si().split()))
A.sort()
def BS(listA,L,R,X):
    result = R+1
    while L<=R:
        mid = (L+R)//2
        if listA[mid] < X:
            L = mid + 1
        else:
            result = mid
            R = mid - 1
    return result

sum_ = 1 << 31
ans1, ans2 = 0,0
for i in range(N-1):
    cand = BS(A,i+1,N-1,-A[i])
    if cand < N and abs(A[i]+A[cand]) < sum_:
        sum_ = abs(A[i]+A[cand])
        ans1, ans2 = A[i],A[cand]
    if cand -1 > i and abs(A[i]+A[cand-1]) < sum_:
        sum_ = abs(A[i]+A[cand-1])
        ans1, ans2 = A[i],A[cand-1]

print(ans1,ans2)

    