""""
부분수열의 합
link: https://www.acmicpc.net/problem/1182
"""

import sys
si = sys.stdin.readline

n,s = list(map(int,si().split()))
numbers = list(map(int,si().split()))
answer = 0

def rec(k,value):
    if k == n:
        global answer
        if value == s:
            answer += 1
    else:
        rec(k+1,value+numbers[k])
        rec(k+1,value)

rec(0,0)
if s==0:
    answer-=1
print(answer)