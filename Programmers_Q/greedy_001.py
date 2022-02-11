"""
체육복
link: https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
velog: 

문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 
체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	        4
3	[3]	    [1]	        2
"""

count = 30
def rec_(k,M,selected,lost,reserve):
    temp_lost = lost.copy()
    global count
    if k == M:
        for i in range(0,M):
            #만약 0이면 앞쪽 친구가 체육복이 없는지 확인 후 빌려준다.
            if selected[i]==0:
                if reserve[i]-1 in temp_lost:
                    temp_lost.remove(reserve[i]-1)
                    
            #만약 1이면 뒷쪽 친구가 체육복이 없는지 확인 후 빌려준다.    
            elif selected[i]==1:
                if reserve[i]+1 in temp_lost:
                    temp_lost.remove(reserve[i]+1)
                    
        if len(temp_lost) <= count:
            count = len(temp_lost)
        
    else:
        for cand in range(0,2):
            selected[k] = cand
            rec_(k+1,M,selected,lost,reserve)
            selected[k] = -1


def solution(n, lost, reserve):
    answer = 0
    global count

    #여벌옷 가져온 학생이 체육복을 잃어버리는 경우
    for x in lost:
        if x in reserve:
            lost.remove(x)
            reserve.remove(x)

    M = len(reserve)
    selected = [-1 for _ in range(M)]

    rec_(0,M,selected,lost,reserve)
    answer = n - count
    return answer


print(solution(5,	[2, 4],	[1, 3, 5]))
print(solution(5,	[2, 4],	[3]))
print(solution(3,   [3], [1]))


"""
def solution(n, lost, reserve):
    
    # lost와 reserve에 같은 수가 있다면 제거
    for x in lost:
        if x in reserve:
            lost.remove(x)
            reserve.remove(x)
    
    answer = n - len(lost)

    while True:
        temp = answer
        for x in lost:
            if x+1 in reserve and x-1 not in reserve:
                answer += 1
                reserve.remove(x+1)
                lost.remove(x)
            elif x-1 in reserve and x+1 not in reserve:
                answer += 1
                reserve.remove(x-1)
                lost.remove(x)
        if answer == temp: break
    
    for x in lost:
        if x-1 in reserve:
            answer += 1
            reserve.remove(x-1)
        elif x+1 in reserve:
            answer += 1
            reserve.remove(x+1)
    
    return answer

"""