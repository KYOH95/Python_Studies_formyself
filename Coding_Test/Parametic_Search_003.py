#boj_1654
#parametic search
#랜선 자르기
import sys
si = sys.stdin.readline
K,N = map(int,si().split())
K_list = []
for _ in range(K):
    K_list.append(int(si()))


def val_check(length):
    sum = 0
    for x in K_list:
        sum += x//length
    return sum >= N

L = 1
R = max(K_list)
ans = 0
while L <= R:
    M = (L+R)//2
    if val_check(M):
        ans = M
        L = M+1
    else: R = M-1

print(ans)