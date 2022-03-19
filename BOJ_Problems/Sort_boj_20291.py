"""
파일 정리
link: https://www.acmicpc.net/problem/20291
"""

import sys
si = sys.stdin.readline

N = int(si())

dict_ = {}
for i in range(N):
    temp = (si().split('.')[1]).split()[0] 
    if temp not in dict_:
        dict_[temp] = 1
    else:
        dict_[temp] += 1

for x in sorted(dict_,key = lambda x:x):
    print(x,dict_[x])
    