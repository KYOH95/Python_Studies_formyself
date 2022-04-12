"""
타겟 넘버
link: https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

"""
answer = 0
def rec(k, num, target, selected, sign):
    global answer
    if k == len(num):
        if sum(selected) == target:
            answer += 1
    else:
        for i in sign:
            selected[k] = num[k] * i
            rec(k+1, num, target, selected, sign)
            selected[k] = 0

def solution(numbers, target):
    global answer
    selected = [0 for _ in range(len(numbers))]
    sign = [-1,1]
    rec(0, numbers,target, selected, sign)
    return answer

# print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))