"""
랜선 자르기
link: https://www.acmicpc.net/problem/1654
"""

import sys
si = sys.stdin.readline
K, N = list(map(int,si().split()))
K_list = []
for _ in range(K):
    K_list.append(int(si()))

def check(value):
    count = 0
    for x in K_list:
        count += x//value
    return count >= N

def BS(L,R):
    ans = L-1
    while L <= R:
        mid = (L+R)//2
        if check(mid):
            ans = mid
            L = mid+1
        else:
            R = mid-1
    return ans

print(BS(1,max(K_list)))