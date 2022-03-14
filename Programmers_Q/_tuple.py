"""
튜플
Link: https://programmers.co.kr/learn/courses/30/lessons/64065
"""

def solution(s):
    answer = []
    s_dict = {}
    s_list = s[2:-2].split("},{")
    
    for i in s_list:
        temp = i.split(',')
        for j in temp:
            if j in s_dict:
                s_dict[j] += 1
            else:
                s_dict[j] = 1

    for key,value in sorted(s_dict.items(), key=lambda x: x[1], reverse=True):
        answer.append(int(key))
    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))