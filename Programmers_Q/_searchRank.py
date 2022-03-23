"""
순위 검색
link: https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
"""

def solution(info, query):
    answer = []
    info_list = [[] for _ in range(len(info))]
    query_list = [[] for _ in range(len(query))]
    for i in range(len(info)):
        info_list[i] = info[i].split()
    
    for i in range(len(query)):
        query_list[i] = query[i].split()

    answer = []
    for q in query_list:
        count = 0
        for info in info_list:
            check = 0
            if q[0] != '-':
                if q[0] == info[0]: check+=1
            else: check+=1
            if q[2] != '-':
                if q[2] == info[1]: check+=1
            else: check+=1
            if q[4] != '-':
                if q[4] == info[2]: check+=1
            else: check+=1
            if q[6] != '-':
                if q[6] == info[3]: check+=1
            else: check+=1
            if int(q[7]) <= int(info[4]) and check == 4: 
                count += 1
        answer.append(count)
    return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])