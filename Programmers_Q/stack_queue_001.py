

from collections import deque
def solution(progresses, speeds):
    answer = []
    Q_list = []
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count+=1 
        Q_list.append(count)
    
    Q = deque(Q_list)
    count = 1
    temp = Q[0]
    Q.popleft()
    while len(Q) > 0:
        if Q[0] <= temp:
            count += 1
        else:
            answer.append(count)
            count = 1
            temp = Q[0]
        if len(Q) == 1:
            answer.append(count) 
        Q.popleft()

    return answer
print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
