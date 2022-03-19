"""
단어 정렬
link: https://www.acmicpc.net/problem/1181
"""

import sys
si = sys.stdin.readline

N = int(si())
words = set()
for i in range(N):
    words.add(si().split()[0])

list_ = []
for x in words:
    list_.append(x)

list_.sort(key = lambda x:(len(x),x))
for x in list_:
    print(x)