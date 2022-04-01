"""
숫자카드2
link: https://www.acmicpc.net/problem/10816
"""

import sys
si = sys.stdin.readline

N = int(si())
N_list = list(map(int,si().split()))
M = int(si())
M_list = list(map(int,si().split()))
answer = []

dict = {}
for x in N_list:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1

for x in M_list:
    if x in dict:
        print(dict[x],end=" ")
    else:
        print(0,end=" ")
