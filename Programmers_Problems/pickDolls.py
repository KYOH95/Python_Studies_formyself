"""
크레인 인형뽑기 게임
link: https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
"""

def solution(board,moves):
    cnt = 0
    empty_ = []
    for x in moves:
        for i in range(len(board[x-1])):
            if board[i][x-1] != 0:
                empty_.append(board[i][x-1])
                board[i][x-1] = 0
                break
        if len(empty_)>=2 and empty_[-1] == empty_[-2]:
            empty_.pop()
            empty_.pop()
            cnt += 2

    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],	[1,5,3,5,1,2,1,4]))
print(solution([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0], [0, 2, 1, 0, 0]], [1, 2, 3, 3, 2, 3, 1]))


"""
from collections import deque
def solution(board, moves):
    count = 0
    list_ = [[] for _ in range(5)]
    #세로로 한줄씩 리스트 배열 만들기
    for i in range(5):
        for j in range(5):
            if board[j][i] != 0:
                list_[i].append(board[j][i])
    
    #list_ deque에 넣어주기
    Q = [[] for _ in range(6)]
    for i in range(5):
        Q[i+1] = deque(list_[i])
    
    empty_ = []
    for x in moves:
        if Q[x]:
            if not empty_:
                empty_.append(Q[x][0])
                Q[x].popleft()
            else:    
                if empty_[-1] == Q[x][0]:
                    count += 2
                    empty_.pop()
                else:
                    empty_.append(Q[x][0])
                Q[x].popleft()
    
    return count
"""