#두수의 합

import sys
si = sys.stdin.readline

N = si()
N_list = list(si().split())
X = si()

N_list.sort()

def binary_search(list,i,X,L,R):
    while L <= R:
        M = (L+R)//2
        if list[M] == i:
            #
            continue
        if list[M] + i == X:







    return 0

count = 0
for i in range(N):
    if binary_search(N_list,i,X,0,N-1):
        count+=1