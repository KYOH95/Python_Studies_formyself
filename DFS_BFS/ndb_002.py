# sep/26/2021

#미로탈출
#input: 5 6             output:10(최소 칸수)
#   101010  (0은 괴물 1은 길)
#   111111
#   000001
#   111111
#   111111

N,M = map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,(input()))))


def dfs(x,y):
    pass


count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1
