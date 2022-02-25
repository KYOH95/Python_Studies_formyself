"""
괄호 회전하기
link: https://programmers.co.kr/learn/courses/30/lessons/76502
"""
def check(s_list):
	temp = []
	left = ["(","[","{",]
	for x in s_list:
		# print(x,"___",temp)
		if x in left:
			temp.append(x)
		else:
			if not temp: return 0
			if temp[-1] in left:
				if temp[-1] == "(" and x==")": temp.pop()
				elif temp[-1] == "[" and x=="]": temp.pop()
				elif temp[-1] == "{" and x=="}": temp.pop()
				else: temp.append(x)
			else:
				return 0
	if len(temp) == 0: return 1
	return 0

from collections import deque
def solution(s):
	answer = 0
	queue = deque(s)
	for i in range(len(s)):
		answer += check(queue)
		queue.append(queue[0])
		queue.popleft()
	
	return answer


print(solution("[](){}"))
