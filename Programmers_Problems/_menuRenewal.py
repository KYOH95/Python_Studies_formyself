

dict_menu = {}

def getSetMenu(k,M,order,selected):
    global dict_menu
    if k == M:
        tempID = ''
        for x in selected:
            tempID += order[x]

        if tempID in dict_menu:
            dict_menu[tempID] += 1
        else: 
            dict_menu[tempID] = 1

    else:
        if k == 0: start = 0
        else: start = selected[k-1] + 1
        for cand in range(start,len(order)):
            selected[k] = cand
            getSetMenu(k+1,M,order,selected)


def solution(orders, course):
    answer = []
    global dict_menu
    
    for n in course:
        selected = [0 for _ in range(n)]
        for order in orders:
            order = sorted(order)
            if len(order) >= n:
                getSetMenu(0,n,order,selected)

    max_list = []
    for n in course:
        temp_list = []
        for key, value in dict_menu.items():
            if len(key) == n:
                temp_list.append(value)
            else:
                temp_list.append(2)
        max_list.append(max(temp_list))
    
    for n in range(0,len(course)):
        for key, value in dict_menu.items():
            if len(key) == course[n] and value == max_list[n]:
                answer.append(key)
    
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],	[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],	[2,3,4]))