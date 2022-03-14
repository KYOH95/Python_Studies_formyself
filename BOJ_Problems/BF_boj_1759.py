"""
암호만들기
link: https://www.acmicpc.net/problem/1759
vlog: https://velog.io/@kakasi18/Brute-Force-Boj1759-%EC%95%94%ED%98%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0
"""

import sys
si = sys.stdin.readline

L,C = list(map(int,si().split()))
letters = sorted(list(si().split()))
selected = [0 for _ in range(L)]
used = [False for _ in range(C)]
vowel = ['a','e','i','o','u']

def rec(K):
	if K == L:
		count = 0
		temp = ''
		for i in selected:
			temp += letters[i]
			if letters[i] in vowel: count += 1
		if count >= 1 and count < L-1:
			print(temp)
	else:
		if K == 0: start = 0
		else: start = selected[K-1] + 1
		for cand in range(start,C):
			selected[K] = cand
			rec(K+1)
			selected[K] = -1

rec(0)


