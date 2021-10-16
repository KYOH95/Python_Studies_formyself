#boj_20166
#문자열 지옥에 빠진 호석

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

h,w,k = map(int,si().split())

a = [[]for _ in range(h)]
for i in range(h):
    a[i] = list(si().strip())

k_list = [[]for _ in range(k)]
for i in range(k):
    k_list[i] = list(si().strip())

dir = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
def dfs(cand,x,y,k):
    if k == len(cand)-1: 
        global sum
        sum += 1
        print(i,j,sum)
        k-=1
    
    for dx,dy in dir:
        nx = x+dx
        ny = y+dy
        if nx == -1: nx = h-1
        if nx == h: nx = 0
        if ny == -1: ny = w-1
        if ny == w: ny = 0
        if a[nx][ny] == cand[k+1]:
            dfs(cand,nx,ny,k+1)
            k -= 1

sum = 0
ans = 0
for cand in k_list:
    for i in range(h):
        for j in range(w):
            if a[i][j] == cand[0]:
                dfs(cand,i,j,0)
