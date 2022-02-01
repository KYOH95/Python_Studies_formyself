'''
DFS와 BFS
link: https://www.acmicpc.net/problem/1260


문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

'''

import sys
si = sys.stdin.readline
from collections import deque

N,M,start = list(map(int,si().split()))
list_ = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,si().split())
    list_[a].append(b)
    

visited = [0 for _ in range(N+1)]

def DFS(start):
    visited[start] = 1
    print(start,end = " ")

    for x in list_[start]:
        if visited[x] == 1: continue
        DFS(x)
        

DFS(start)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
"""