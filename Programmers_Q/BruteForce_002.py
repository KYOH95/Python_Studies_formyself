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

list_ = ['1','2','7']
used = [0,0,0]
selected = []
def rec_func(k):
    temp = ''
    if k == len(list_):
        print("HIT")
    for cand in range(0,len(list_)):
        if used[cand]: continue
        temp = list_[cand]
        used[cand] = 1
        if list_[cand] not in selected:
            selected.append(list_[cand])
        
        rec_func(k+1)
        used[cand] = 0
        temp = ''

    print(selected)
            
rec_func(0)


# def rec_fucn(k):
#     if k == M:
#         for x in selected:
#             print(x,end='')
#         print()
#     else:
#         for cand in range(1,N+1):
#             if used[cand]:
#                 continue
#             selected[k] = cand
#             used[cand] = 1
#             rec_fucn(k+1)
#             selected[k] = 0
#             used[cand] = 0


# def solution(numbers):

#     #만들 수 있는 모든 숫자의 리스트 
#     numbers_list = []
#     list_allNumbers = []

#     for x in numbers:
#         numbers_list.append(str(x))
#         list_allNumbers.append(str(x))

    
        
    
#     #소수인가?
#     # answer = 0
#     # print(answer)
#     return 0
    

