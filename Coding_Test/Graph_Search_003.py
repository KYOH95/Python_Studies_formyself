#boj1012
#유기농 배추
import sys
si = sys.stdin.readline
sys.setrecursionlimit(100000)

#            상 하 좌 우
direction = [[0,-1],[0,1],[-1,0],[1,0]]

def dfs(x,y):
    visited[x][y] = True
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
        if visited[nx][ny]: continue
        if K_list[x][y] == 0: continue
        dfs(nx,ny)

T = int(si())
while T:
    T-=1
    M,N,K = map(int,si().split())
    K_list = [[0]*M for _ in range(N)]

    for _ in range(K):
        a,b = map(int,si().split())
        K_list[b][a] = 1

    count = 0
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] or K_list[i][j]==0: continue
            count += 1
            dfs(i,j)
            
    print(count)


