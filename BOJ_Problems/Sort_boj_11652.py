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

print(list_)
