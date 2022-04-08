"""
고냥이
link: https://www.acmicpc.net/problem/16472
"""

import sys
si = sys.stdin.readline

N = int(si())
word = si()[:-1]
count = [0] * 200
kind = 0

def add(x):
    global kind
    count[ord(x)] += 1
    if count[ord(x)] == 1: kind += 1

def sub(x):
    global kind
    count[ord(x)] -= 1
    if count[ord(x)] == 0: kind -= 1

L = 0
ans = 0
for R in range(len(word)):
    add(word[R])
    while kind > N:
        sub(word[L])
        L+=1
    ans = max(ans, R-L+1)

print(ans)
