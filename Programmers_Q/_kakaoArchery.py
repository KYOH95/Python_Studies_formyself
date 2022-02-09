"""
양궁대회
link: https://programmers.co.kr/learn/courses/30/lessons/92342?language=python3

"""

answer_selected = [-1]
difference_ = 0
lowest_num = [0,0]
def rec_(k,M,selected,info):
    global answer_selected
    global difference_
    global lowest_num
    sum_R = 0
    sum_A = 0

    if k == M:
        for i in range(0,11):
            if selected.count(i) > info[i]:
                sum_R += (10-i)
            elif selected.count(i) <= info[i] and info[i] >= 1:
                sum_A += (10-i)
        
        if sum_R > sum_A and (sum_R - sum_A) >= difference_:
            #만약 점수가 같다면
            if sum_R - sum_A == difference_:
                if max(selected) > lowest_num[0]:
                    difference_ = (sum_R - sum_A)
                    answer_selected = selected.copy()
                    lowest_num.append([max(selected),selected.count(max(selected))])
                elif max(selected) == lowest_num[0]:
                    if selected.count(max(selected)) >= lowest_num[1]:
                        difference_ = (sum_R - sum_A)
                        answer_selected = selected.copy()
                        lowest_num.append([max(selected),selected.count(max(selected))])
            else:
                difference_ = (sum_R - sum_A)
                answer_selected = selected.copy()
                lowest_num.append([max(selected),selected.count(max(selected))])
            
    else:
        if k == 0: start = 0
        else: start = selected[k-1]
        for cand in range(start,11):
            selected[k] = cand
            if selected.count(cand) <= info[cand] +1:
                rec_(k+1,M,selected,info)
                selected[k] = -1


def solution(n, info):
    global answer_selected
    answer = [0 for _ in range(11)]
    selected = [-1 for _ in range(n)]
    
    rec_(0,n,selected,info)
    
    if answer_selected == [-1]: return [-1]
    for x in answer_selected:
        answer[x] += 1

    return answer


# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))