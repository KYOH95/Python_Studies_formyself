# 9/20/2021

#음료수 얼려먹기 문제

#input: 4 5                 output: 3  (덩어리 갯수 찾기)
#     : 00110
#     : 00011
#     : 11111
#     : 00000

from collections import deque

N,M = map(int,input().split())
graph = []

for i in range(N):
    graph.append(input())


# print(graph[0][0])

visited = [[0 for i in range(M)] for i in range(N)]

print(visited)

def ice_cream(graph,visited):
    
    queue = deque([0][0])
    
    for i in range(M):
        for j in range(N):
            pass