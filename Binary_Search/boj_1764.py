#boj_1764
#듣보잡

import sys
si = sys.stdin.readline

N,M = map(int,input().split())
N_list = []
M_list = []

for i in range(N):
    N_list.append(si())

for i in range(M):
    M_list.append(si())

A = sorted(N_list)
B = sorted(M_list)

def binary_search(list,x,L,R):
    while L<=R:
        M = (L+R)//2
        if list[M] == x:
            return True
        if x < list[M]: R = M-1
        else: L = M+1
    return False


ans = []
count = 0
for x in A:
    if binary_search(B,x,0,M-1):
        count += 1
        ans.append(x)

print(count)
for x in ans: 
    print(x)