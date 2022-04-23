# 미로 탐색
# link: https://www.acmicpc.net/problem/2178

import sys
from collections import deque
si = sys.stdin.readline
N,M = list(map(int,si().split()))
a = [si().strip() for _ in range(N)]
dir = [[1,0],[-1,0],[0,-1],[0,1]]

dist = [[0] * M for _ in range(N)]
dist[0][0] = 1
def bfs():
    queue = deque()
    queue.append(0)
    queue.append(0)
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if dist[nx][ny] != 0: continue
            if a[nx][ny] == '0': continue
            dist[nx][ny] = dist[x][y] + 1
            queue.append(nx)
            queue.append(ny)
        
bfs()
print(dist[N-1][M-1])
