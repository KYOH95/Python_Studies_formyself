"""
프린터
link: https://programmers.co.kr/learn/courses/30/lessons/42587?language=python3#

"""
def solution(priorities, location):
    answer_list = []
    index = []
    
    #index 리스트에 인덱스 넣어주기
    for i in range(len(priorities)):
        index.append(i)

    #prioirities 리스트가 0일때까지 루프 
    while len(priorities) > 0:
        #만약 첫번째 인덱스에 있는 priorities가 가장 크다면 answer_list에 그수의 인덱스를 push
        if priorities[0] == max(priorities):
            answer_list.append(index[0])
        #그렇지 않다면 가장뒤로 push
        else:
            index.append(index[0])
            priorities.append(priorities[0])
        priorities.pop(0)
        index.pop(0)
    
    #answer_list에서 location과 같은 수의 인덱스를 answer에 +1해준다.
    for i in range(len(answer_list)):
        if answer_list[i]==location:
            return i+1
    
print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 7, 1, 1],0))
print(solution([3,1,3,2],2))
print(solution([9,9,0,9,9],2))