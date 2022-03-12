"""
N-Queen
link: https://www.acmicpc.net/problem/9663
"""

import sys
si = sys.stdin.readline
n = int(si())

answer = 0
row = [0 for _ in range(n)]

def attackable(c1,c2,r1,r2):
	if c1 == c2: return True
	if r1-c1 == r2-c2: return True
	if r1+c1 == r2+c2: return True
	return False

def rec(k,row):
	global answer
	if k==n:
		answer += 1
	else:
		for i in range(n):
			# possible = True
			for j in range(k):
				if attackable(i,row[j],k,j):
					# possible = False
					break
			# if possible:
			row[k] = i
			rec(k+1,row)
			row[k] = 0

rec(0,row)
print(answer)
