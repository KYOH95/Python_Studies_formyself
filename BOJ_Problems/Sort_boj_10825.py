"""
국영수
link: https://www.acmicpc.net/problem/10825
"""

import sys
si = sys.stdin.readline

N = int(si())
score = [[] for _ in range(N)]
for i in range(N):
	score[i] = list(si().split())
	score[i][1:] = map(int,score[i][1:])

score.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))

for x in score:
	print(x[0])
