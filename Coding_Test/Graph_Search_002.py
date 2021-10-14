#boj2667 단지번호 붙이기
import sys
si = sys.stdin.readline
N = int(si())
a = [si().strip() for _ in range(N)]

#DFS
visited = [[0] * N for _ in range(N)]
#            동  / 서 / 남 / 북
direction = [[1,0],[-1,0],[0,1],[0,-1]]

def dfs(x,y):
    global group_count
    group_count += 1
    visited[x][y] = 1
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        if visited[nx][ny]: continue
        if a[nx][ny] == '0': continue
        dfs(nx,ny)

groups = []
for i in range(N):
    for j in range(N):
        if visited[i][j] or a[i][j]=='0': continue
        group_count = 0
        dfs(i,j)
        groups.append(group_count)

groups.sort()
print(len(groups))
for x in groups:
    print(x)