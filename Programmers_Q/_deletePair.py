"""
짝지어 제거하기

"""

def solution(s):
    answer = 0
    s_list = []
    for x in s:
        s_list.append(x)
    
    while True:
        count = 0
        if len(s_list) <= 1: break
        for i in range(len(s_list)-1):
            if s_list[i] == s_list[i+1]:
                s_list.pop(i+1)
                s_list.pop(i)
                count += 1
                break
                
        if count == 0:
            break
    
    if len(s_list) == 0:
        answer = 1
    return answer

print(solution("baabaa"))