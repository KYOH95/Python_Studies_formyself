# 스택/큐 기능개발

from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = []
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            queue.append((100-progresses[i]) // speeds[i])
        else:
            queue.append((100-progresses[i]) // speeds[i] + 1)

    Q = deque(queue)
    day = Q[0]
    cnt = 0
    while Q:
        if Q[0] <= day:
            cnt += 1
        else:
            day = Q[0]
            answer.append(cnt)
            cnt = 1

        if len(Q) == 1:
            answer.append(cnt)
        Q.popleft()

    return answer