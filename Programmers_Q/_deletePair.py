"""
짝지어 제거하기

"""
from collections import deque
def solution(s):
    answer = 0
    
    Q = deque(s)
    boolCheck = False
    while len(Q)>1:
        temp = []

        while True:
            count = len(Q)
            if len(Q) == 1:
                temp.append(Q[0])
                break
            
            if Q[0] == Q[1]:
                Q.popleft()
                Q.popleft()
            else:
                temp.append(Q[0])
                Q.popleft()

            if count == len(Q):
                boolCheck = True
            if len(Q) == 0: break
        
        Q = deque(temp)
        if boolCheck == True: break
        
    if len(Q)==0:
        answer = 1
    
    return answer
print(solution("cdcd"))