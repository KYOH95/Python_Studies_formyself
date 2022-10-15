# 짝지어 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    queue = []
    for x in s:
        if bool(queue) and queue[-1]==x:
            queue.pop()
        else:
            queue.append(x)
            
    if bool(queue): return 0
    else: return 1