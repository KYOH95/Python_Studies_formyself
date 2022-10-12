# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    word_list = list(map(str, s.split(" ")))
    
    for word in word_list:
        answer += word.capitalize()
        answer += ' '
            
    return answer[:-1]


print(solution("3people unFollowed me"))