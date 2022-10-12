# 코딩테스트 연습 연습문제 [다음 큰 숫자]
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    m = n+1
    bin_1_count = bin(n).count("1")
    while True:
        if bin(m).count("1") == bin_1_count:
            return m
        m+=1
