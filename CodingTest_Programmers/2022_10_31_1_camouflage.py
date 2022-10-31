# 코딩테스트 연습 해시 "위장"
# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    dict_clothes = {}
    for i in clothes:
        if i[1] not in dict_clothes:
            dict_clothes[i[1]] = 2
        else:
            dict_clothes[i[1]] += 1
    
    answer = 1
    for value in dict_clothes.values():
        answer *= value
    
    return answer-1