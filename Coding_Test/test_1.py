# import sys
# from collections import deque
# sys.setrecursionlimit(100000)
# si = sys.stdin.readline





def solution(board):
    N = len(board)

    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    def dfs(x,y):
        # if visited[x][y]: return 0
        visited[x][y] = True
        # global count
        for dx,dy in dir:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if visited[nx][ny]: continue
            if board[nx][ny] != board[x][y]: continue
            visited[nx][ny] = True
            # count += 1
            dfs(nx,ny)

    def count_True(cnt):
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    cnt += 1
        return cnt

    max = 0
    for i in range(N):
        visited = [[False] * N for _ in range(N)]
        for j in range(N):
            dfs(i,j)
            cnt = 0
            cnt = count_True(cnt)
            if cnt >= max: max = cnt   
    
    for i in range(N):
        visited = [[False] * N for _ in range(N)]
        for j in range(N):
            dfs(j,j)
            cnt = 0
            cnt = count_True(cnt)
            if cnt >= max: max = cnt   
                

    answer = max
    print(answer)
    return answer

solution(['ABBBBC', 'AABAAC', 'BCDDAC', 'DCCDDE', 'DCCEDE', 'DDEEEB'])