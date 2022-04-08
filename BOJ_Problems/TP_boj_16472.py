"""
고냥이
link: https://www.acmicpc.net/problem/16472
"""

from collections import deque
import sys
si = sys.stdin.readline

N = int(si())
word = si()[:-1]
dict = {}

sum = 0
ans = 0
R = 0
for L in range(len(word)):
    ans = max(sum,ans)
    while R < len(word) and len(dict)<= N:
        R += 1
        if word[R] in dict:
            dict[word[R]] += 1
        else:
            dict[word[R]] = 0
        
        sum += 1
    print(sum)
    sum -= 1
    dict[word[L]] -= 1
    if word[L] == 0: del dict[word[L]]

print(ans)


    