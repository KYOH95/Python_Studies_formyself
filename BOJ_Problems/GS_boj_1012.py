#유기농 배추
#link: https://www.acmicpc.net/problem/1012

import sys
si = sys.stdin.readline
sys.setrecursionlimit(100000)
T = int(si())
ans = []
direction = [[1,0],[-1,0],[0,-1],[0,1]]

#배추 묶음 구하는 함수
def dfs(x,y):
    visited[x][y] = 1
    for dx,dy in direction:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny <0 or nx >= N or ny >= M: continue
        if visited[nx][ny]: continue
        if a[nx][ny] == 0: continue
        dfs(nx,ny)

#테스트 케이스 만큼 열어보기
for _ in range(T):
    M,N,K = list(map(int,si().split()))
    a = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        x,y = list(map(int,si().split()))
        a[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 0: continue #배추가 없는 곳은 건너뛰기
            if visited[i][j]: continue #방문한 곳은 건너뛰기
            dfs(i,j)
            count += 1
    ans.append(count)
    
for x in ans:
    print(x)