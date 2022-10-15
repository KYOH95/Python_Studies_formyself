# 구명보트
# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)
    while q:
        answer += 1
        if q[0] + q[-1] <= limit:
            q.pop()
        if q: 
            q.popleft()
    return answer