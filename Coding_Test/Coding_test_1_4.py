#boj_20167
#호석애벌레

import sys
from collections import deque
si = sys.stdin.readline


N,K = map(int,si().split())
a = list(map(int,si().split()))

def calculate(i):
    global sum
    global ans
    global start
    while True:
        if i == len(a):
            if sum >= K: sum -= K
            start = i
            return sum
        if sum >= K:
            sum -= K
            start = i
            return sum
        sum += a[i]
        i+=1

ans = 0
sum = 0
start = 0
while True:
    if start == len(a): break
    ans += calculate(start+1)

print(ans)
