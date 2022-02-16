"""
프린터
link: https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3#

"""

def solution(priorities, location):
    answer = 1
    answer_list = []
    index_list = priorities
    while True:
        if len(priorities) == 0: break
        if priorities[0] == max(priorities):
            answer_list.append(priorities[0])
            priorities.pop(0)
        else:
            priorities.append(priorities[0])
            priorities.pop(0)
            
    
    print(answer_list)
    return answer
    
# solution([2, 1, 3, 2],2)
solution([1, 1, 9, 1, 7, 1, 1],0)
# solution([3,1,3,2],2)