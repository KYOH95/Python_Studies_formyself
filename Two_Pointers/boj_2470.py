#boj_2470
#두용액

import sys
si = sys.stdin.readline

N = int(si())
a = sorted(list(map(int,si().split())))

ansL = 1000000000
ansR = -1000000000
sum = 2000000000
L = 0
R = N-1
while L < R:
    if a[L] + a[R] == 0:
        ansL = a[L]
        ansR = a[R]
        break
    elif a[L] + a[R] < 0:
        if abs(a[L]+a[R]) < sum:
            ansL = a[L]
            ansR = a[R]
            sum = abs(a[L]+a[R])
        L+=1
    else:
        if abs(a[L]+a[R]) < sum:
            ansL = a[L]
            ansR = a[R]
            sum = abs(a[L]+a[R])
        R-=1
    
print(ansL,ansR)
        