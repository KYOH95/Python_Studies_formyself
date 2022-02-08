

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
            if len(order) >= n:
                getSetMenu(0,n,order,selected)

    # for n in course:
    #     for key, value in dict_menu.items():
    #         if len(key) == n and value = max()
            
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],	[2,3,4])