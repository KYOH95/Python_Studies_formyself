"""
짝지어 제거하기

"""

from collections import deque
def solution(s):
    answer = 0
    s_list = [s[0]]
    
    for x in s[1:]:
        if len(s_list)==0:
            s_list.append(x)
        else:
            if x == s_list[-1]:
                s_list.pop()
            else:
                s_list.append(x)
    
    if len(s_list) == 0: 
        answer = 1
    return answer

print(solution("bbabba"))
print(solution("cdcd"))