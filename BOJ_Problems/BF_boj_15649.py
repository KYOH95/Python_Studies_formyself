"""
N과M(1)
link: https://www.acmicpc.net/problem/15649
"""

import sys
si = sys.stdin.readline

N,M  = list(map(int,si().split()))

def rec(K,M,N,selected,used):
	if K == M:
		for x in selected:
			print(x,end = " ")
		print()
	else:
		for cand in range(N):
			if used[cand] == False:
				selected[K] = cand + 1
				used[cand] = True
				rec(K+1,M,N,selected,used)
				used[cand] = False
				selected[K] = 0

selected = [0 for _ in range(M)]
used = [False for _ in range(N)]
rec(0,M,N,selected,used)
