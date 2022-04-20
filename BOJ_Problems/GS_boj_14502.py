#연구소
#link: https://www.acmicpc.net/problem/14502

import sys
from collections import deque
si = sys.stdin.readline

N,M = list(map(int,si().split()))
lab = [list(map(int,si().split())) for _ in range(N)]
ans = 0

def bfs():
    global ans
    visited = [[0]*M for _ in range(N)]
    dir = [[1,0],[-1,0],[0,-1],[0,1]]

    Q = deque()
    for i in range(N):
        for j in range(M):
            if lab[i][j]==2:
                visited[i][j]=1
                Q.append(i)
                Q.append(j)
    
    while Q:
        x = Q.popleft()
        y = Q.popleft()
        
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny] == 1: continue
            if lab[nx][ny] != 0: continue
            visited[nx][ny] = 1
            Q.append(nx)
            Q.append(ny)
        
    count = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j]== 0 and not visited[i][j]: count += 1

    ans = max(ans,count)


blankQ = deque()
for i in range(N):
    for j in range(M):
        if lab[i][j]==0:
            blankQ.append(i)
            blankQ.append(j)


blank = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

wallCount = 0
def dfs(idx,wallCount):
    if wallCount == 3:
        bfs()
        return
    
    if idx == len(blank):
        return
    
    lab[blank[idx][0]][blank[idx][1]] = 1
    dfs(idx+1,wallCount+1)

    lab[blank[idx][0]][blank[idx][1]] = 0
    dfs(idx+1,wallCount)

dfs(0,0)
print(ans)