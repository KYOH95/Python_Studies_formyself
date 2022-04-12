"""
오픈채팅방


"""


def solution(record):
    answer = []
    dic_rec = {}
    list_ = []
    
    # record의 기록들을 ' '기준으로 잘랐을때 행동, 유저아이디, 이름 으로 정리할 수 있다. dict에 키값에 유저아이디를, value값에 이름을 저장한다.
    for i in record:
        act = i.split()[0]
        uid = i.split()[1]
        list_.append([act,uid])
        if act != "Leave":
            dic_rec[uid] = i.split()[2] #최종적으로 마지막 이름이 유저아이디에 저장

	#저장한 유저아이디 dict를 바탕으로 Enter와 Leave를 구분하여 정답리스트에 계속해서 더해준다.
    for i in list_:
        if i[0] == "Enter":
            answer.append("%s님이 들어왔습니다."%(dic_rec[i[1]]))
        elif i[0] == "Leave":
            answer.append("%s님이 나갔습니다."%(dic_rec[i[1]]))
    
    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))