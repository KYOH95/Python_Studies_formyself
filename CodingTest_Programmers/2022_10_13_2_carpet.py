# 코딩테스트 연습 완전탐색 [카펫]
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    for i in range(1,int(yellow**(1/2))+1):
        if yellow%i==0:
            if (yellow//i+i)*2 + 4 == brown:
                return [(yellow//i)+2,i+2]