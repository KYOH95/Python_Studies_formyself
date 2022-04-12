"""
완주하지 못한 선수
link: https://programmers.co.kr/learn/courses/30/lessons/42576
velog: 

문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

"""


# 내가 직접 작성한 코드
# def solution(participant, completion):
#     # 완주자 dict
#     cmpt_dict = {runner: 0 for runner in completion}
#     for runner in completion:
#         cmpt_dict[runner] += 1
    
#     # 참가자 dict
#     part_dict = {people: 0 for people in participant}
#     for people in participant:
#         part_dict[people] += 1

#     # 완주하지 못한 사람 찾기
#     for key in part_dict:
#         if key not in cmpt_dict: return key 
#         else:
#             if part_dict[key] != cmpt_dict[key]: return key

    
# print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))


#해시를 이용하여 다시 작성하는 코드

def solution(participant, completion):
    
    dict = {}
    temp = 0

    for runner in participant:
        dict[hash(runner)] = runner
        temp += hash(runner)

    for cRunner in completion:
        temp -= hash(cRunner) 

    answer = dict[temp]
    return answer


print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))