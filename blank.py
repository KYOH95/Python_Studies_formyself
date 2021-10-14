#practice

import sys
from collections import deque
# sys.setrecursionlimit(100000)
si = sys.stdin.readline

h,w = map(int,input().split())
a = [list(si().strip()) for _ in range(h)]

print(a[0][0],a[h-1][w-1])
print(h,w)