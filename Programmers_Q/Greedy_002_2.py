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

def solution(number, k):
    answer = ''
    start = 0
    count = len(number) - k
    while k > 0:        
        max = 0
        temp_start = start
        end = start+ k+1
        print(start,end)
        for i in range(start,end):
            if int(number[i]) > max:
                max = int(number[i])
                start = i + 1

        answer += str(max)
        # print(temp_start,start)
        k -= start-1 - temp_start

    count -= len(answer)
    if count > 0:
        for i in range(len(number)-count,len(number)):
            answer += number[i]
    return answer


# solution("1924",2)
# solution("1231234",3)
print(solution("4177252841",4))


# def solution(number, k):
#     answer = ''
    
#     start_max = int(number[0])
#     start_index = 0

#     for i in range(0, k+1):
#         print("i =",i, "max =", start_max)

#         if int(number[i]) > start_max:
#             start_max = int(number[i])
#             start_index = i
#             break

#     count = k - start_index
#     answer += number[start_index]
#     for i in range(start_index+1, len(number)-1):
#         if count == 0: 
#             mid = i
#             break
#         if number[i] < number[i+1]:
#             count -= 1
#         else:
#             answer += number[i]

#     if count == 0:
#         for i in range(mid,len(number)):
#             answer += number[i]


#     print("hit")
#     print(start_max,start_index,count)
#     print(answer)
#     return answer