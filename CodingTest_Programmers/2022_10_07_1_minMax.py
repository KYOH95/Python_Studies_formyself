# 연습문제 > 최댓값과 최솟값

def solution(s):
    answer = ''

    s = s.split(" ")
    s = list(map(int, s))
    answer = str(min(s))
    answer += " "
    answer += str(max(s))

    return answer

print(solution("-1 -2 -3 -4"))