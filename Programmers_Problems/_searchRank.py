"""
순위 검색
link: https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
"""

def check(q,info,i):
    if q[0] != '-':
        if q[0] != info[i][0]: return False
    if q[1] != '-':
        if q[1] != info[i][1]: return False
    if q[2] != '-':
        if q[2] != info[i][2]: return False
    if q[3] != '-':
        if q[3] != info[i][3]: return False
    return True

def bs(list_i,l,r,x):
    result = r+1
    while l <= r:
        mid = (l+r)//2
        # print(mid)
        if list_i[mid] >= x:
            r = mid-1
            result = mid
        else: #list_i[mid] >= x:
            l = mid+1
    return result

def solution(info, query):
    answer = []
    info_list = [[] for _ in range(len(info))]
    query_list = [[] for _ in range(len(query))]
    infoScore = []

    for i in range(len(info)):
        info_list[i] = info[i].split()
        infoScore.append(int(info_list[i][4]))
    
    for i in range(len(query)):
        query[i] = query[i].replace(" and "," ")
        query_list[i] = query[i].split()

    info_list.sort(key = lambda x:int(x[4]))
    infoScore.sort()
    for q in query_list:
        sum = 0
        for i in range(bs(infoScore,0,len(infoScore)-1,int(q[4])),len(info)):
            if check(q,info_list,i):
                sum += 1
        answer.append(sum)

    return answer



# def solution(info, query):
#     answer = []
#     info_list = [[] for _ in range(len(info))]
#     query_list = [[] for _ in range(len(query))]
#     for i in range(len(info)):
#         info_list[i] = info[i].split()
    
#     for i in range(len(query)):
#         query_list[i] = query[i].split()

#     answer = []
#     for q in query_list:
#         count = 0
#         for info in info_list:
#             check = 0
#             if q[0] != '-':
#                 if q[0] == info[0]: check+=1
#             else: check+=1
#             if q[2] != '-':
#                 if q[2] == info[1]: check+=1
#             else: check+=1
#             if q[4] != '-':
#                 if q[4] == info[2]: check+=1
#             else: check+=1
#             if q[6] != '-':
#                 if q[6] == info[3]: check+=1
#             else: check+=1
#             if int(q[7]) <= int(info[4]) and check == 4: 
#                 count += 1
#         answer.append(count)
#     return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])