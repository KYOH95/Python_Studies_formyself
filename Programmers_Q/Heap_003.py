"""
이중 우선순위 큐
link: https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
"""

import heapq
def solution(operations):
	answer = []
	heap = []

	for x in operations:
		op = x.split()[0]
		num = int(x.split()[1])
		
		if op == "I":
			heapq.heappush(heap,num)
		else:
			if not heap: continue
			if num == -1:
				heapq.heapify(heap)
				heapq.heappop(heap)
			else:
				heapq._heapify_max(heap)
				heapq._heappop_max(heap)

	if not heap:
		return [0,0]
	else:
		heapq._heapify_max(heap)
		answer.append(heap[0])
		heapq.heapify(heap)
		answer.append(heap[0])

	return answer

print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))
