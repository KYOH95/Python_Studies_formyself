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

count = 0
max = 0
answer = 0
for i in range(1,N):
    if list_[i] == list_[i-1]:
        count += 1
    else: 
        if count > max:
            max = count
            answer = list_[i-1]
        count = 0

if count > max:
            max = count
            answer = list_[i-1]

print(answer)
