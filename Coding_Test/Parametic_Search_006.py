#6236
#용돈관리

import sys
si = sys.stdin.readline

N,M = map(int,si().split())
N_list = []

for _ in range(N):
    N_list.append(int(si()))


def val_check(amount):
    sum = 0
    count = 1
    for x in N_list:
        if x + sum > amount:
            sum = x
            count += 1
        else:
            sum += x
    return count <= M

L = max(N_list)
R = 1000000000
ans = 0
while L <= R:
    mid = (L+R)//2
    if val_check(mid):
        ans = mid
        R = mid - 1
    else: L = mid + 1

print(ans)

