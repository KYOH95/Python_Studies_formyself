# 단지번호붙이기
# link: https://www.acmicpc.net/problem/2667

import sys
si = sys.stdin.readline

N = int(si())
map_ = [0 for _ in range(N)]
for i in range(N):
    map_[i] = si().strip()

visited = [[0] * N for _ in range(N)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
ans = []

def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = 1
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        if visited[nx][ny] == 1: continue
        if map_[nx][ny]=='0': continue
        dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1: continue
        if map_[i][j] == '0': continue
        cnt = 0
        dfs(i,j)
        ans.append(cnt)

ans.sort()
print(len(ans))
for x in ans:
    print(x)
     