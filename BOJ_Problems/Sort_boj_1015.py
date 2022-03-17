"""
수열 정렬
link: https://www.acmicpc.net/problem/1015
"""

import sys
si = sys.stdin.readline
N = int(si())
A = list(map(int,si().split()))

sortList = [[] for _ in range(N)]
#입력 받은 리스트 A의 값과 그 인덱스를 함께 저장해준다.
for i in range(N):
    sortList[i].append(i)
    sortList[i].append(A[i])

#A의 값을 기준으로 정렬해준다.
sortList.sort(key = lambda x:x[1])

#정렬된 리스트에 다시 한번 현재 인덱스(P값)를 append 해준다.
for i in range(N):
    sortList[i].append(i)

#가장 처음 리스트 A의 인덱스 순서대로 정렬 후, 마지막에 구한 P값을 출력한다.
for x in sorted(sortList,key = lambda x:x[0]):
    print(x[2], end = ' ')

