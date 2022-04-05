"""
List of Unique Numbers
link: https://www.acmicpc.net/problem/13144
"""

import sys
si = sys.stdin.readline
N = int(si())
N_list = list(map(int,si().split()))
count = [0] * 100001

R = -1
ans = 0
sum = 0
for L in range(N):
    while R+1 < N and count[N_list[R+1]] == 0:
        R += 1
        count[N_list[R]] += 1
        sum += 1
    ans += sum
    sum -= 1
    count[N_list[L]] -= 1

print(ans)
