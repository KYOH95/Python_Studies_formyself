#boj_1026
#보물

import sys
si = sys.stdin.readline

N = int(si())
a = list(map(int,si().split()))
b = list(map(int,si().split()))

a.sort()
b.sort(reverse = True)

s = 0
for i in range(N):
    s += a[i]*b[i]

print(s)