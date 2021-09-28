# sep/26/2021

#미로탈출
#input: 5 6             output:10(최소 칸수)
#   101010  (0은 괴물 1은 길)
#   111111
#   000001
#   111111
#   111111
from collections import deque 


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # print(queue)
 
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

    return graph[N-1][M-1]
                

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

#    상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]


print(bfs(0,0))
print(graph)