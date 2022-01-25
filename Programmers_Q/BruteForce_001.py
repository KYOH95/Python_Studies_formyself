"""
[완전탐색] 모의고사
Link: https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
velog: https://velog.io/@kakasi18/ProgrammersBrute-Force%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC

문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers return
[1,2,3,4,5][1]
[1,3,2,4,2][1,2,3]
"""

def solution(answers):

    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {id: 0 for id in range(1,4)}

    for i in range(0,len(answers)):
        if answers[i] == list_1[i%5]: count[1] += 1
        if answers[i] == list_2[i%8]: count[2] += 1
        if answers[i] == list_3[i%10]: count[3] += 1

    count_list = sorted(count, key = lambda x: (-count[x],x))

    answer = []
    max_ = count[count_list[0]]
    for x in count_list:
        if count[x] == max_:
            answer.append(x)

    return answer

print(solution([1,3,2,4,2]))
print(solution([1,1]))