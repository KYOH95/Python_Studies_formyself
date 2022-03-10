"""
연산자 끼워넣기
link: https://www.acmicpc.net/problem/14888
"""

import sys
si = sys.stdin.readline

N = int(si())
numbers = list(map(int,si().split()))
operators = list(map(int,si().split()))
op_list = []

for i in range(4):
	for _ in range(operators[i]):
		op_list.append(i)

selected = [[] for i in range(N-1)]
used = [False for i in range(N-1)]

def rec(K,numbers, op_list, used, value):
	if K == len(op_list):
		print(selected)
	else:
		for i in range(4):
			if used[i] == False:
				selected[K] = [i,numbers[i+1]]
				used[i] = True
				rec(K+1,numbers, op_list, used, value)
				selected[K] = [-1,-1]
				used[i] = False

rec(0,numbers,op_list,used,0)






