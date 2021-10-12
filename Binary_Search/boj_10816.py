#boj_10816
#숫자카드2

import sys
si = sys.stdin.readline

N = int(si())
listN = sorted(list(map(int,si().split())))
M = int(si())
listM = list(map(int,si().split()))

def lower_bound(listN,x,L,R):
    res = R+1
    while (L<=R):
        M = (L+R)//2
        if listN[M] >= x: 
            res = M
            R = M-1
        else: L = M+1
    return res

def upper_bound(listN,x,L,R):
    res = R+1
    while (L<=R):
        M = (L+R)//2
        if listN[M] > x: 
            res = M
            R = M-1
        else: L = M+1
    return res

for x in listM:
    print(upper_bound(listN,x,0,N-1)-lower_bound(listN,x,0,N-1),end=' ')