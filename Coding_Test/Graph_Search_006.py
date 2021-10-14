#boj_3184
#양

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

h,w = map(int,si().split())
map_ = [[0] for _ in range(h)]
for i in range(h):
    map_[i] = list(si().strip())

direction = [[0,1],[0,-1],[1,0],[-1,0]]
def DFS(x,y):
    visited[x][y] = True
    global wolves, sheeps
    if map_[x][y] == 'v': wolves+=1
    if map_[x][y] == 'o': sheeps+=1
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
        if visited[nx][ny]: continue
        if map_[nx][ny] == '#': continue
        DFS(nx,ny)

final_sheeps = 0
final_wolves = 0
visited = [[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        wolves = 0
        sheeps = 0
        if visited[i][j]: continue
        if map_[i][j] == '#': continue
        visited[i][j] = True
        DFS(i,j)
        if sheeps > wolves:
            final_sheeps += sheeps
        else:
            final_wolves += wolves

print(final_sheeps, final_wolves)

'''
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###

'''