"""
땅따먹기
https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3
"""

def solution(land):
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1],land[i-1][2],land[i-1][3])
        land[i][1] += max(land[i-1][0],land[i-1][2],land[i-1][3])
        land[i][2] += max(land[i-1][0],land[i-1][1],land[i-1][3])
        land[i][3] += max(land[i-1][0],land[i-1][1],land[i-1][2])
    
    return max(land[len(land)-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
print(solution([[1,1,1,1],[2,2,2,3], [3,3,3,6], [4,4,4,7]]))


# def getMax(land,startIndex):
#     sum = land[0][startIndex]
#     last = startIndex
#     for i in range(1,len(land)):
#         temp = land[i].copy()
#         temp.remove(land[i][last])
#         sum += max(temp)
#         last = land[i].index(max(temp))
#     return sum

# def solution(land):
#     answer = []
#     for i in range(4):
#         answer.append(getMax(land,i))
    
#     print(answer)
#     return max(answer)






# # 재귀함수로 풀었을때 (런타임 에러가 남)
# import sys
# sys.setrecursionlimit(1000001)
# answer = 0
# def rec(K,land,selected):
#     if K == len(land):
#         global answer
#         temp = 0
#         for i in range(len(selected)):
#             temp += land[i][selected[i]]
#         if temp > answer:
#             answer = temp
#     else:
#         for cand in range(4):
#             if selected[K] != 0:
#                 if cand == selected[K-1]: continue
#             selected[K] = cand
#             rec(K+1,land,selected)
#             selected[K] = -1

# def solution(land):
#     global answer
#     selected = [-1 for _ in range(len(land))]
#     rec(0,land,selected)
#     return answer

# print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))