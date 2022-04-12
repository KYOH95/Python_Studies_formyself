"""
소수 찾기
link: https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3
velog: 

문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
"17"	3
"011"	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

11과 011은 같은 숫자로 취급합니다.
"""


answer_list = [] #소수인지 확인해볼 정답리스트

# 소수인지 확인하는 함수
def primeNumber(num):
    if num <= 1:
        return 0
    for i in range(2,int(num**(0.5))+1):
        if num % i == 0:
            return 0
    return 1

#소수확인 전 가능한 모든 숫자들을 찾고 리스트에 담아주는 재귀함수
def rec_fucn(k,m,n,selected,used,numbers):
    global answer_list
    #만약 m개의 자리만큼 선택했다면, temp에 임시로 숫자를 담아주고 answer_list에 존재하는지 확인 후 없다면 append()
    if k == m:
        temp = ''
        for x in selected:
            temp += numbers[x]
        if int(temp) not in answer_list:
            answer_list.append(int(temp))

    else:
        for i in range(n):
            if used[i]:
                continue
            selected[k] = i
            used[i] = 1
            rec_fucn(k+1,m,n,selected,used,numbers)
            selected[k] = -1
            used[i] = 0

#메인 함수
def solution(numbers):
    global answer_list
    answer = 0
    
    #1의 자리부터 n개 자리까지 확인하며 rec_fucn을 호출
    for i in range(1,len(numbers)+1):
        selected = [-1 for _ in range(i)] # 선택할 리스트
        used = [0 for _ in range(len(numbers))] # 중복 방지를 위한 사용확인 리스트
        rec_fucn(0,i,len(numbers),selected,used,numbers)

    #정답 리스트에 담긴 모든 수들을 소수인지 확인하며, 소수면 정답을 +1씩 해줌
    for x in answer_list:
        answer += primeNumber(x)
    
    return answer

print(solution("17"))
print(solution("011"))