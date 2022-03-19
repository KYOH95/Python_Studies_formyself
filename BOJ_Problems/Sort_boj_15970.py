"""
화살표 그리기
link: https://www.acmicpc.net/problem/15970
"""

import sys
si = sys.stdin.readline
answer = 0
N = int(si())
AB = [[] for _ in range(N)]
dict_AB = {}

#dictionary에 색별로 좌표 저장하기
for i in range(N):
    AB[i] = list(map(int,si().split()))
    if AB[i][1] in dict_AB:
        dict_AB[AB[i][1]].append(AB[i][0])
    else:
        dict_AB[AB[i][1]] = [AB[i][0]]

#왼쪽 좌표와의 거리
def left(list_,i):
    if i == 0: return 100000
    else: return list_[i] - list_[i-1]

#오른쪽 좌표와의 거리
def right(list_,i):
    if i == len(list_)-1: return 100000
    else: return list_[i+1]-list_[i]

#최소거리 계산 후 정답
for value in sorted(dict_AB.values()):
    temp = sorted(value)
    sum = 0
    for i in range(len(temp)):
        sum += min(left(temp,i),right(temp,i))
    answer += sum

print(answer)
    


