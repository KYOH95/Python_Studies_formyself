#코딩테스트 연습
# 스택/큐
# 올바른 괄호

# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = 0
    
    for i in s:
        if i == "(":
            stack += 1
        else:
            stack -= 1
            if stack < 0: return False
    
    if stack == 0: return True
    else: return False
    