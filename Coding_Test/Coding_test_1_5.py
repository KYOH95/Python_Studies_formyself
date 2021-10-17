#boj_20168
#골목대장호석

import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

N,M,A,B,money = map(int,si().split())

M_list = [[]for _ in range(M+1)]
for _ in range(M):
    x,y,c = map(int,si().split())
    M_list[x].append(y)
    M_list[x].append(c)
    M_list[y].append(x)
    M_list[y].append(c)

# print(N,M,start,end,money)
# print(M_list)

def bfs(start,end):
    visited[start] = True
    queue = deque()
    queue.append(start)
    queue.append(max_toll[start])
    queue.append(sum_toll[start])

    while queue:
        x = queue.popleft()
        cur_max = queue.popleft()
        cur_toll = queue.popleft()
        for i in range (0,len(M_list[x]),2):
            if M_list[x][i] == end:
                if money >= cur_toll + cur_max:
                    visited[M_list[x][i]] = True
                    if max_toll[M_list[x][i]] > cur_max: 
                        ans.append(max_toll[M_list[x][i]])
                    else: ans.append(cur_max)
                
            else:
                if visited[M_list[x][i]]: continue
                if M_list[x][i] > cur_max: max_toll[M_list[x][i]] = M_list[x][i+1]
                sum_toll[M_list[x][i]] = M_list[x][i+1] + cur_toll
                visited[M_list[x][i]] = True
                queue.append(M_list[x][i])
                queue.append(M_list[x][i+1])
                queue.append(sum_toll[M_list[x][i]])

visited = [False for _ in range(N+1)]
max_toll = [0 for _ in range(N+1)]
sum_toll = [0 for _ in range(N+1)]
ans = []
bfs(A,B)

print(visited)
print(max_toll)
print(sum_toll)
print(ans)




















# toll = [0 for _ in range(N+1)]
# visited = [False for _ in range(N+1)]
# def dfs(x,y,max):
#     visited[x] = True
#     if x == y:
#         return
#     for i in range(0,len(M_list[x]),2):
#         if M_list[x][i] == y:
#             global ans
#             if M_list[x][i+1] > max:
#                 max = M_list[x][i+1]
#             if toll[x] + M_list[x][i+1] <= money:
#                 ans.append(max)
#                 visited[M_list[x][i]] = True
#             break
#         else:
#             if visited[M_list[x][i]]: continue
#             if toll[M_list[x][i]]!=0: continue
#             if M_list[x][i+1] > max: max = M_list[x][i+1]
#             visited[M_list[x][i]] = True
#             toll[M_list[x][i]] = toll[x] + M_list[x][i+1]
#             dfs(M_list[x][i],y,max)

# ans = []
# dfs(start,end,0)

# if not visited[end]: ans.append(-1)
# print(min(ans))
