"""
먹을 것인가 먹힐 것인가
link: https://www.acmicpc.net/problem/7795 
"""

import sys
si = sys.stdin.readline
T = int(si())

def BS(list_,L,R,X):
	result = L-1
	while L <= R:
		M = (L+R)//2
		if list_[M] < X:
			result = M
			L = M+1
		else:
			R = M-1
	return result

def runTest():
	Asize,Bsize = map(int,si().split())
	A = list(map(int,si().split()))
	B = list(map(int,si().split()))
	B.sort()

	answer = 0
	for x in A:
		answer += BS(B,0,Bsize-1,x) + 1
	print(answer)

for _ in range(T):
	runTest()
