"""
여행경로
link: https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
"""

from collections import deque
def solution(tickets):
	answer = [tickets[0][0]]
	start = tickets[0][0]
	dict_ = {}
	for x in tickets:
		if x[0] in dict_:
			dict_[x[0]].append(x[1])
		else:
			dict_[x[0]] = [x[1]]

	for x in dict_:
		dict_[x] = deque(sorted(dict_[x]))

	while dict_:
		answer.append(dict_[start][0])
		temp = dict_[start][0]
		dict_[start].popleft()
		if not dict_[start]:
			dict_.pop(start,None)
		start = temp
		
	return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))



# dict_['ICN'].popleft()
# dict_['ICN'].popleft()
# dict_['SFO'].popleft()
# dict_['ATL'].popleft()
# dict_['ATL'].popleft()
# dict_.pop('ICN', None)
# dict_.pop('SFO', None)
# dict_.pop('ATL', None)