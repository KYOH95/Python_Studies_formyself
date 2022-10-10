# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    del_cnt = 0
    loop = 0
    while (s!="1"):        
        loop += 1
        next_s = 0
        
        #제거할 0의 개수
        del_cnt += s.count("0")
        next_s = s.count("1")
                
        #이진 변환 결과
        s = format(next_s, 'b')
        
    return [loop,del_cnt]

print(solution("110010101001"))