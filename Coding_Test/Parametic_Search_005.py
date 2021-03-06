#boj_2343
#기타레슨
import sys
si = sys.stdin.readline
N,M = map(int,si().split())
N_list = list(map(int,si().split()))

L = max(N_list)
R = 10000000000
ans = 0

def val_check(D):
    sum = 0
    count = 1 
    for x in N_list:
        if sum + x <= D:
            sum += x
        else:
            sum = x
            count += 1
        # print(D,count,sum)
    
    return count <= M

while L <= R:
    mid = (L+R)//2
    if val_check(mid):
        ans = mid
        R = mid - 1
    else: L = mid + 1

print(ans)