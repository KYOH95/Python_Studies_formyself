"""
카드
link: https://www.acmicpc.net/problem/11652
"""

import sys
si  = sys.stdin.readline
N = int(si())

list_ = [0 for _ in range(N)]

for i in range(N):
    list_[i] = int(si())

list_.sort()

count = 1
max = 1
answer = list_[0]
#앞의 리스트 값과 같으면 count를 늘려가고, 다르면 max값과 비교하여 정답 구하기 + count값 초기화
for i in range(1,N):
    if list_[i] == list_[i-1]:
        count += 1
    else: 
        if count > max:
            max = count
            answer = list_[i-1]
        count = 1

#제일 마지막에 확인 못한것 
if count > max:
    max = count
    answer = list_[-1]

print(answer)
