"""
약수의 개수와 덧셈

Link: https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3

문제 설명
두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000
입출력 예
left	right	result
13	17	43
24	27	52
입출력 예 설명
입출력 예 #1

다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.
수	약수	약수의 개수
13	1, 13	2
14	1, 2, 7, 14	4
15	1, 3, 5, 15	4
16	1, 2, 4, 8, 16	5
17	1, 17	2
따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.
"""

#약수구하는 함수
def getDvisor(num):
        sum = 1
        for i in range(2,num+1):
            if num % i == 0:
                sum += 1
        return sum


def solution(left, right):
    answer = 0
    
    for x in range(left,right+1):
        #만약 약수의 갯수가 홀수 이면 빼주기, 짝수면 더하기
        if getDvisor(x) % 2 == 1:
            answer -= x
        else:
            answer += x
        
    return answer

print(solution(13,	17))
print(solution(24,	27))