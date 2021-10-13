#boj_2110
#공유기 설치
import sys
si = sys.stdin.readline
N,C = map(int,si().split())
N_list = []

for _ in range(N):
    N_list.append(int(si()))

def val_check(D):
    count = 1
    last = N_list[0]
    for i in range(1,N):
        if N_list[i] - last >= D: 
            last = N_list[i]
            count+=1
    return count >= C

L = 1
R = max(N_list)
ans = 0
N_list.sort()
while L <= R:
    mid = (L+R)//2
    if val_check(mid):
        ans = mid
        L = mid + 1
    else:
        R = mid - 1

print(ans)

