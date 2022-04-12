"""
행렬 테두리 회전하기
link: https://programmers.co.kr/learn/courses/30/lessons/77485
"""

def rotate(map,q):
    temp = map[q[0]-1][q[1]-1]
    min_list = [map[q[0]-1][q[1]-1]]
    #left side
    for i in range(q[0]-1,q[2]-1):
        map[i][q[1]-1] = map[i+1][q[1]-1]
        min_list.append(map[i+1][q[1]-1])

    #bottom side
    for i in range(q[1]-1,q[3]-1):
        map[q[2]-1][i] = map[q[2]-1][i+1]
        min_list.append(map[q[2]-1][i+1])

    #right side
    for i in range(q[2]-1,q[0]-1,-1):
        map[i][q[3]-1] = map[i-1][q[3]-1]
        min_list.append(map[i-1][q[3]-1])

    #top side
    for i in range(q[3]-1,q[1]-1,-1):
        map[q[0]-1][i] = map[q[0]-1][i-1]
        min_list.append(map[q[0]-1][i-1])
    map[q[0]-1][q[1]] = temp
    return min(min_list)

def solution(rows, columns, queries):
    answer = []
    map = [[0 for _ in range(columns)] for _ in range(rows)] 
    count = 0
    for i in range(rows):
        for j in range(columns):
            count +=1
            map[i][j] = count
    for i in range(len(queries)):
        answer.append((rotate(map,queries[i])))
    return answer


print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))