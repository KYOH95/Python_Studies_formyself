"""
여행경로
link: https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
"""

answer = []
def rec(k,dict_,tickets,selected,used_,start):
	if k == len(tickets):
		for x in selected:
			answer.append(x)
		return 0
	else:
		for i in range(len(dict_[start])):
			if not used_[start][i]:
				selected[k] = dict_[start][i]
				used_[start][i] = True
				rec(k+1,dict_,tickets,selected,used_,dict_[start][i])
			
def solution(tickets):
	global answer
	start = tickets[0][0]
	answer.append(start)
	dict_ = {}
	used_ = {}
	for x in tickets:
		if x[0] in dict_:
			dict_[x[0]].append(x[1])
		else:
			dict_[x[0]] = [x[1]]

	for x in dict_:
		dict_[x] = sorted(dict_[x])
		used_[x] = [False for _ in range(len(dict_[x]))]

	selected = ['' for _ in range(len(tickets))]
	rec(0,dict_,tickets,selected,used_,start)
	return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
