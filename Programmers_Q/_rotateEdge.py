"""
행렬 테두리 회전하기
link: https://programmers.co.kr/learn/courses/30/lessons/77485
"""


def rotate(map,q):

    print(q[0],q[1],q[2],q[3])
    temp = map[q[1]-1][q[3]-1]
    for i in range(q[2]-1,q[0]-2,-1):
        print(map[i][q[1]])


def solution(rows, columns, queries):
    answer = []
    map = [[0 for _ in range(columns)] for _ in range(rows)] 
    count = 1
    for i in range(rows):
        for j in range(columns):
            map[i][j] = count
            count +=1
    
    rotate(map,queries[0])
        





    return answer


solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])