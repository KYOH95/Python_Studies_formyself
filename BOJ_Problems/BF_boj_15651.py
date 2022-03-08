"""
N과M(3)
link: https://www.acmicpc.net/problem/15651
"""

import sys
si = sys.stdin.readline
N,M = list(map(int,si().split()))

def rec(K,M,N,selected):
	if K == M:
		for x in selected:
			print(x,end= " ")
		print()
	else:
		for cand in range(1,N+1):
			selected[K] = cand
			rec(K+1,M,N,selected)

selected = [0 for _ in range(M)]
rec(0,M,N,selected)
