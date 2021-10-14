#14502
#연구소

#3개의 벽위치를 완전 탐색을 할때마다 BFS를 사용하여 넓이를 구한다!

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

h,w = map(int,si().split())
map_ = [[]for _ in range(h)]
for i in range(h):
    map_[i] = list(map(int,si().split()))

empty = []
for i in range(h):
    for j in range(w):
        if map_[i][j] == 0:
            empty.append([i,j])

# print(empty)

def bfs():
    visited = [[False]* w for _ in range(h)]
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    count = 0
    global ans

    queue = deque()
    for i in range(h):
        for j in range(w):
            if map_[i][j]==2:
                visited[i][j]=True
                queue.append(i)
                queue.append(j)
    
    while queue:
        x = queue.popleft()
        y = queue.popleft()

        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
        
            if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
            if visited[nx][ny]: continue
            if map_[nx][ny] != 0: continue
            visited[nx][ny] = True
            queue.append(nx)
            queue.append(ny)

    for i in range(h):
        for j in range(w):
            if map_[i][j]==0 and not visited[i][j]:
                count += 1
    
    if count > ans: ans = count



def dfs(index,selected_cnt):
    if selected_cnt == 3:
        bfs()
        return

    if index == len(empty): return

    map_[empty[index][0]][empty[index][1]] = 1
    dfs(index+1,selected_cnt+1)
    
    map_[empty[index][0]][empty[index][1]] = 0
    dfs(index+1,selected_cnt)

ans = 0
dfs(0,0)
print(ans)


'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

'''