"""
연산자 끼워넣기
link: https://www.acmicpc.net/problem/14888
"""

import sys
si = sys.stdin.readline

N = int(si())
num = list(map(int,si().split()))
op_temp = list(map(int,si().split()))
selected = ['_' for _ in range(N-1)]

op_fixed = ['+','-','*','/']
op_list = []
used = [False for _ in range(N-1)]

for i in range(4):
	for _ in range(op_temp[i]):
		op_list.append(op_fixed[i])

def rec(K):
	if K == N-1:
		print(selected)
	else:
		if K == 0: start = 0
		else: start = selected[K] + 1
		for i in range(start,N-1):
			if used[i] == False:
				selected[i] = i
				used[i] = True
				rec(K+1)
				selected[i] = ' '
				used[i] = False

rec(0)



