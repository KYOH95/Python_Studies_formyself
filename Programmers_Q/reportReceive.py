"""
프로그래머스: [카카오] 신고 결과 받기

link: https://programmers.co.kr/learn/courses/30/lessons/92334
velog: 

입출력 예
id_list	report	k	result
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3	[0,0]


"""

def solution(id_list, report, k):

    rpt_dict = {id: [] for id in id_list}
    cnt_dict = {id: 0 for id in id_list}

    #신고당한 사람 중복없이 dict 리스트 만들기
    for user in report:
        if user.split()[0] in rpt_dict[user.split()[1]]:
            break
        else: rpt_dict[user.split()[1]].append(user.split()[0])
    # print(rpt_dict)

    #신고당한 user의 갯수가 k 이상인지 확인하고 id_dict 에 답장 메일 갯수 추가하기
    for reported in rpt_dict:
        if len(rpt_dict[reported]) >= k:
            for user in rpt_dict[reported]:
                cnt_dict[user] += 1


    answer = []
    for value in cnt_dict.values():
        answer.append(value)
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))

"""better Answer:
def solution(id_list, report, k):

    #신고당한 사람 중복없이 dict 리스트 만들기
    rpt_dict = {id: set() for id in id_list}
    for each in report:
        user_id, report_id = each.split()
        rpt_dict[report_id].add(user_id)
        

    #신고당한 user의 갯수가 k 이상인지 확인하고 id_dict 에 답장 메일 갯수 추가하기
    cnt_dict = {id: 0 for id in id_list}
    for key,values in rpt_dict.items():
        if len(values) >= k:
            for value in values:
                cnt_dict[value] += 1

    return list(cnt_dict.values())
"""






