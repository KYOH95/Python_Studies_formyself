#boj_2470
#두용액

import sys
si = sys.stdin.readline

N = int(si())
N_list = sorted(list(map(int,si().split())))


def bs(list,x,L,R):
    res = R+1
    while L<=R:
        M = (L+R)//2
        if list[M] >= x:
            res = M
            R = M - 1
        else: L = M + 1
    return res

sum = 1 << 31
v1,v2 = 0,0
for i in range(N-1):
    cand = bs(N_list,-N_list[i],i+1,N-1)
    if i < cand -1 and abs(N_list[i] + N_list[cand-1]) < sum:
        sum =  abs(N_list[i] + N_list[cand-1])
        v1 = N_list[i]
        v2 = N_list[cand-1]
    
    if cand < N and abs(N_list[i] + N_list[cand]) < sum:
        sum =  abs(N_list[i] + N_list[cand])
        v1 = N_list[i]
        v2 = N_list[cand]

print(v1,v2)
