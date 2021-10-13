#boj_2805
#나무자르기

import sys
si = sys.stdin.readline
N,M = map(int,si().split())
N_list = list(map(int,si().split()))

def valueCheck(H):
    sum = 0
    for x in N_list:
        if x - H > 0:
            sum += x - H
    return sum >= M

L = 0
R = 2000000000
ans = 0
while L <= R:
    mid = (L+R)//2
    if valueCheck(mid): # 높은 숫자 범위로 체크
        L = mid+1
        ans = mid
    else: 
        R = mid-1

print(ans)