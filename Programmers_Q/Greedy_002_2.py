"""
큰 수 만들기
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
입출력 예
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"

"""

from collections import deque
def solution(number, k):
    answer = ''
    #만약 number가 일의 자리이면, 그 수 그대로 return
    if len(number) == 1:
        return number

    #Q스택을 이용한다.
    Q = deque(number)
    #제거해야하는 갯수가 0이되면 while 루프를 나간다.
    while k>0:
        #제거될 수 없을 수도 있으니 미리 방지하기
        temp = k

        # 만약 9라면 뒤에 숫자 보지 않고 바로 넘어가주기
        if Q[0] == '9':
            answer += str(Q[0])
            Q.popleft()
            continue
        
        #뒤에 존재하는 숫자가 더 크면 앞에 숫자 제거, k도 늘려주기
        for i in range(1, k+1):
            if int(Q[0]) < int(Q[i]):
                Q.popleft()
                k -= 1
                break
        
        #제거한 숫자가 없다면 가장 앞에 스택 빼주고 answer에 append
        if temp == k:
            answer += str(Q[0])
            Q.popleft()
        
        #만약 answer의 길이가 현재 남아있는 큐스택 - k보다 크다면 즉시 loop에서 break
        if len(answer) > len(Q) - k:
            break
    
    #스택에 남아있는 문자 answer에 append
    for x in Q:
        answer += x
    
    #만약 정답의 길이가 number에서 k만큼 제거한 수보다 길때, 잘라주기
    if len(answer) > len(number) - k:
        temp = ''
        for i in range(0,len(number)-k):
            temp += answer[i]
        return temp

    return answer


solution("1924",2)
solution("1231234",3)
print(solution("4177252841",4))


# def solution(number, k):
#     answer = ''
#     start = 0
#     count = len(number) - k
#     while k > 0:        
#         max = 0
#         temp_start = start
#         end = start+ k+1
#         print(start,end)
#         for i in range(start,end):
#             if int(number[i]) > max:
#                 max = int(number[i])
#                 start = i + 1

#         answer += str(max)
#         # print(temp_start,start)
#         k -= start-1 - temp_start

#     count -= len(answer)
#     if count > 0:
#         for i in range(len(number)-count,len(number)):
#             answer += number[i]
#     return answer