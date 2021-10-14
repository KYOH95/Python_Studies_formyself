
# Note

"""
1초에 1억번 연산 가능

if N = 100,000
N^2 = 10,000,000,000(약 100억) -> 약 100초 걸림

Binary Search
Nlog(N) = 10만 * 5 = 50만


-21억 < Integer 범위 < 21억


"""


#-----------------------------------------------------------------

"""[1] Slicing"""
# Index: list[0,1,2,3,4]
# Index: list[-4,-3,-2,-1]
# list[-1] = 리스트 마지막에 있는 자료

# delete: list[:-1] 마지막 하나 제거
# reverse: list[::-1] step을 거꾸로 하나씩 해서 처음부터 끝까지 돌려라
#           [ 시작 : 끝 : 스텝]

#-----------------------------------------------------------------

"""[2] Sort"""

# list.sort(key = lambda x:(x[1],-x[2]))
#                           1번째 우선순위 x[1]에 대하여 오름차순
#                           2번째 우선순위 x[2]에 대하여 내림차순 
#                       
#-----------------------------------------------------------------

"""[3] input"""
import sys
si = sys.stdin.readline
# A = int(si())
# B = si()
# print(A,end='')
# print(B)

# print(type(A))

#-----------------------------------------------------------------

"""[4} Graphs & BFS|DFS"""
sys.setrecursionlimit(100000)
#인접행렬:  O(V^2)
#인접리스트: O(E)

"""DFS: Queue 없음"""
#recursive function을 통해서 찾아낸다
N = int(si())
a = [si().strip() for _ in range(N)]
visit = [[False] * N for _ in range(N)]


"""BFS: Queue 있음"""
#     Queue가 비어있을 때까지 반복한다
# 큐스텍에 쌓아서 찾아낸다. while문으로
from collections import deque
# key words: 최소이동횟수 || 최단 시간

# queue = deque()
# queue.append(x)
# queue.popleft()

