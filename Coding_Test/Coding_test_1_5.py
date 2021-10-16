#boj_20168
#골목대장호석

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

N,M,start,end,money = map(int,si().split())

M_list = [[]for _ in range(M+1)]
for _ in range(M):
    x,y,c = map(int,si().split())
    M_list[x].append(y)
    M_list[x].append(c)
    M_list[y].append(x)
    M_list[y].append(c)

toll = [0 for _ in range(M+1)]
visited = [False for _ in range(M+1)]
def dfs(x,y,max):
    visited[x] = True
    if x == y:
        return
    for i in range(0,len(M_list[x]),2):
        if M_list[x][i] == y:
            global ans
            if M_list[x][i+1] > max:
                max = M_list[x][i+1]
            if toll[x] + M_list[x][i+1] <= money:
                ans.append(max)
                visited[M_list[x][i]] = True
            break
        else:
            if visited[M_list[x][i]]: continue
            if toll[M_list[x][i]]!=0: continue
            if M_list[x][i+1] > max: max = M_list[x][i+1]
            visited[M_list[x][i]] = True
            toll[M_list[x][i]] = toll[x] + M_list[x][i+1]
            dfs(M_list[x][i],y,max)

ans = []
dfs(start,end,0)

if not visited[end]: ans.append(-1)
print(min(ans))
