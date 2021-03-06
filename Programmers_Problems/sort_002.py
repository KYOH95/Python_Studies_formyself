"""


link:
velog : https://velog.io/write?id=aa3e9003-2e90-464b-b2f2-4b8a518ae171

문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

Ex)
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"

"""
import functools

def compare(a,b):
    if int(str(a)+str(b)) > int(str(b)+str(a)): return 1
    elif int(str(a)+str(b)) < int(str(b)+str(a)): return -1
    else: return 0 # a == b

def solution(numbers):
    answer = ''
    numbers.sort(key = functools.cmp_to_key(compare), reverse = True)
    
    sum = 0
    for x in numbers:
        answer += str(x)
        sum += x
    
    if sum == 0: return str(0)
    else: return answer


# numbers = [6,10,2]
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))