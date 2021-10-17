
import sys
from collections import deque
sys.setrecursionlimit(100000)
si = sys.stdin.readline

N = int(si())
a = [[]for _ in range(N)]
for i in range(N):
    a[i] = list(map(int,si().split()))


a.sort(key = lambda x:(x[0],x[1]))
max = 0
for i in range(N-1):
    count = 1
    start = i+1
    temp = a[i][1]
    for j in range(start,N):
        if a[j][0] >= temp:
            temp = a[j][1]
            count += 1
    if count > max:
        max = count

print(max)