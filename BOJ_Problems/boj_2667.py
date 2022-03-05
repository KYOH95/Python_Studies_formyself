"""
단지 번호 붙이기
link: https://www.acmicpc.net/problem/2667
"""

graph = ['0110100','0110101','1110101','0000111','0100000','0111110','0111000']
move = [[1,0],[-1,0],[0,-1],[0,1]]
visited = [[False for _ in range(len(graph))]for _ in range(len(graph))]
def dfs(x,y):
    global graph
    global visited
    visited[x][y] = True
    for dx,dy in move:
        next_x = x + dx
        next_y = y + dy
        if next_x < 0 or next_y < 0 or next_x >= len(graph) or next_y >= len(graph): continue
        if graph[next_x][next_y] == '0': continue
        if visited[next_x][next_y] == True: continue
        dfs(next_x,next_y)

def solution():
    answer = 0
    global visited
    global graph
    for i in range(len(graph)):
        for j in range(len(graph)):
            if visited[i][j] == True or graph[i][j]=='0': continue
            answer += 1
            dfs(i,j) 
    return answer
    
print(solution())