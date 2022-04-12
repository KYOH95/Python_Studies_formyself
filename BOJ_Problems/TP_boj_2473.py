# 세 용액
# link: https://www.acmicpc.net/problem/2473

import sys
si = sys.stdin.readline

N = int(si())
a = list(map(int,si().split()))
a.sort()

ans = [0] * 3
sum = sys.maxsize
for i in range(N-2):
    L = i+1
    R = N-1
    while L < R:
        temp = a[i] + a[L] + a[R]
        if abs(temp) < sum:
            sum = abs(temp)
            ans = [a[i],a[L],a[R]]
        if temp < 0: L += 1
        elif temp >0: R -= 1
        else: break
    
print(ans[0],ans[1],ans[2])
