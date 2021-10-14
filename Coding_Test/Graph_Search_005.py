#boj_4963
#섬의 개수
import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

direction = [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[-1,1],[1,1]]
def DFS(x,y):
    visited[x][y] = True
    for dx,dy in direction:
        nx = x+dx
        ny = y+dy
        if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
        if visited[nx][ny]: continue
        if map_[nx][ny] == 0: continue
        DFS(nx,ny)

while True:
    w,h = map(int,si().split())
    map_ = [[]for _ in range(h)]
    for i in range(h):
        map_[i] = list(map(int,si().split()))

    if w==0 and h==0: break

    visited = [[False]*w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] or map_[i][j]==0: continue
            ans += 1
            DFS(i,j)   
    print(ans)

