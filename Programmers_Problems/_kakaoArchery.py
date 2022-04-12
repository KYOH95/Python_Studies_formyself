"""
양궁대회
link: https://programmers.co.kr/learn/courses/30/lessons/92342?language=python3

"""


difference_ = 0
answer = [0 for _ in range(11)]
def rec_(k,M,selected,info):
    global difference_
    global answer
    sum_R = 0
    sum_A = 0

    if k == M:
        #Selected 리스트에 선택된 양궁점수들을 점수로 계산해주기 | sum_R:라이언 점수 sum_A:어피치 점수
        for i in range(0,11):
            if selected.count(i) > info[i]:
                sum_R += (10-i)
            elif selected.count(i) <= info[i] and info[i] >= 1:
                sum_A += (10-i)
        
        # 조건1) 라이언점수가 어피치 점수보다 커야한다.
        # 조건2) 점수차가 전에 기존에 선택되었던 점수보다 더 크거나 같아야한다.
        if sum_R > sum_A and (sum_R - sum_A) >= difference_:
            #만약 기존에 선택되었던 양궁 점수와 점수차가 현재와 같다면 더 낮은 점수를 많이 맞춘 것을 선택한다.
            conditionCheck = True
            if sum_R - sum_A == difference_:
                for x in range(10,-1,-1):
                    #만약 기존에 선택된 양궁 가장 낮은 점수(10번째 인덱스, 0점)의 양궁 갯수가 더 많다면 컨디션을 'False'로 주고 정답이 될 수 없도록 한다.
                    if answer[x] > selected.count(x):
                        conditionCheck = False
                        break
                    #만약 기존에 선택된 양궁 가장 낮은 점수의 양궁 갯수가 더 적다면 컨디션을 'True'로 주고 정답이 될 수 있는 조건이 된다.
                    elif answer[x] < selected.count(x):
                        conditionCheck = True
                        break

            #점수 차이가 더 크다면 
            if conditionCheck == True:
                difference_ = (sum_R - sum_A)
                # answer_selected = sorted(selected).copy()
                answer = [0 for _ in range(11)]
                for x in selected:
                    answer[x] += 1      

    #양궁 점수판 recursive 메소드를 이용하여 선택해주기
    else:
        if k == 0: start = 0
        else: start = selected[k-1]
        for cand in range(start,11):
            selected[k] = cand
            if selected.count(cand) <= info[cand] +1:
                rec_(k+1,M,selected,info)
                selected[k] = -1

def solution(n, info):
    global answer
    selected = [-1 for _ in range(n)]
    
    rec_(0,n,selected,info)

    if answer == [0,0,0,0,0,0,0,0,0,0,0]: return [-1]
    return answer

print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))
