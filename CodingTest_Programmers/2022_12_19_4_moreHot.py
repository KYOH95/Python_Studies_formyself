from heapq import heappush, heappop, heapify
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while True:
        first = heappop(scoville)
        if first > K: break
        if len(scoville) == 0: 
            answer = -1
            break
        second = heappop(scoville)*2
        heappush(scoville,first+second)
        answer += 1
        
    return answer