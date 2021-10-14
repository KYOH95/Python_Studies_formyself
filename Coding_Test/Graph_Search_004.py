#boj_11724
#연결 요소의 개수

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline
N, M = map(int,si().split())
N_list = [[]for _ in range(N+1)]

for _ in range(M):
    x,y = list(map(int,si().split()))
    N_list[x].append(y)
    N_list[y].append(x)

def DFS(x):
    visited[x]=True
    for y in N_list[x]:
        if visited[y]: continue
        DFS(y)


visited = [False for _ in range(N+1)]
ans = 0
for i in range(1,N+1):
    if visited[i]: continue
    ans += 1
    DFS(i)

print(ans)















# def BFS(start):
#     queue = deque()
#     queue.append(start)
#     while queue:
#         x = queue.popleft()
#         visited[x] = True
#         for y in N_list[x]:
#             if visited[y]: continue
#             queue.append(y)

# visited = [False for _ in range(0,N+1)]
# visited[0] = True
# count = 0
# bool_ = True
# while bool_:
#     for i in range(1,N+1):
#         if False not in visited: bool_ = False
#         if visited[i]: continue
#         else: 
#             count += 1
#             BFS(i)

# print(count)
            
        
