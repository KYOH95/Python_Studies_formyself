"""
연산자 끼워넣기
link: https://www.acmicpc.net/problem/14888
"""

import sys
si = sys.stdin.readline
n = int(si())
numbers = list(map(int,si().split()))
operators = list(map(int,si().split()))
answer = []

def calculator(op,val1,val2):
	if op == 0:
		return val1 + val2
	elif op == 1:
		return val1 - val2
	elif op == 2:
		return val1 * val2
	else:
		if val1 < 0:
			return -((-val1//val2))
		else:
			return val1//val2

def rec(k,value):
	global operators
	global numbers
	global answer
	if k == n-1:
		answer.append(value)
	else:
		for i in range(4):
			if operators[i] >= 1:
				operators[i] -= 1
				rec(k+1,calculator(i,value,numbers[k+1]))
				operators[i] += 1

rec(0,numbers[0])
print(max(answer))
print(min(answer))






