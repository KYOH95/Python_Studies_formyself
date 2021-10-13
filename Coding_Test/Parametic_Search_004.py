#boj_2512
#예산
import sys
si = sys.stdin.readline
N = int(si())
N_list = list(map(int,si().split()))
max_ = int(si())

def val_check(value):
    sum = 0
    for x in N_list:
        if x >= value:
            sum += value
        else: sum += x
    return sum <= max_


L = 0
R = max(N_list)
ans = max(N_list)
while L <= R:
    mid = (L+R)//2
    if val_check(mid):
        ans = mid
        L = mid +1
    else: R = mid - 1

print(ans)
