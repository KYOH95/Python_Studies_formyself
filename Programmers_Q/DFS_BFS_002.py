"""
네트워크
link: https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
"""

def DFS(i,n,computers,visited):
    if visited[i] == False:
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1:
                DFS(j,n,computers,visited)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i] == False:
            answer += 1
            DFS(i, n, computers, visited)
    
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
