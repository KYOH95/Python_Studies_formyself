#2178
#미로탐색
import sys
from collections import deque
# sys.setrecursionlimit(100000)
si = sys.stdin.readline

h,w = map(int,si().split())
a = [si().strip() for _ in range(h)]

def bfs(x,y):
    dist = [[0]*w for _ in range(h)]
    dist[x][y] = 1
    dir = [[1,0],[-1,0],[0,1],[0,-1]]
    Q = deque()
    Q.append(x)
    Q.append(y)

    while Q:
        x = Q.popleft()
        y = Q.popleft()
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if nx<0 or nx>=h or ny<0 or ny>=w: continue
            if dist[nx][ny]!=0: continue
            if a[nx][ny]=='0': continue
            dist[nx][ny] = dist[x][y]+1
            Q.append(nx)
            Q.append(ny)
    
    print(dist[h-1][w-1])

bfs(0,0)

"""
4 6
101111
101010
101011
111011

"""

