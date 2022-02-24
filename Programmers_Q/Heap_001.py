
"""
더 맵게
link: https://programmers.co.kr/learn/courses/30/lessons/42626
"""

import heapq
def solution(scoville, K):
	heapq.heapify(scoville)
	answer = 0

	while scoville[0] < K:
		answer += 1
		if len(scoville) == 1:
			return -1
		temp = scoville[0]
		heapq.heappop(scoville)
		temp += scoville[0]*2
		heapq.heappop(scoville)
		heapq.heappush(scoville,temp)
		
	return answer

print(solution([1, 2, 3, 9, 10, 12],7))
