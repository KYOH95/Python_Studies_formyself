"""
다리를 지나는 트럭
link: https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

"""

from collections import deque
def solution(bridge_length, weight, truck_weight):
    sec = 0
    q_distance = deque([bridge_length for _ in range(len(truck_weight))])
    q_weight = deque(truck_weight)
    
    while q_distance:
        sec +=1

        if q_distance[0]<= 0: 
            q_distance.popleft()
            q_weight.popleft()

        sum = 0
        for i in range(0,len(q_distance)):
            sum += q_weight[i]
            if sum <= weight:
                q_distance[i] -= 1
            else: 
                break
        
    return sec

print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))