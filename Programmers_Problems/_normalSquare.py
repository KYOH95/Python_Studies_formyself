"""
멀쩡한 사각형
link: https://programmers.co.kr/learn/courses/30/lessons/62048#qna
"""
def GCF(w,h):
    if w > h: L = h
    else: L = w
    for i in range(L,0,-1):
        if w%i==0 and h%i==0:
            return i

def solution(w,h):
    answer = (w*h)-(w+h-GCF(w,h))
    return answer

print(solution(12,8))
