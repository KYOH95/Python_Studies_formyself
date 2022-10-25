
# O(K * M * N)
# def solution(board, skill):
#     answer = 0
#     for x in skill: 
#         r1,c1,r2,c2=x[1],x[2],x[3],x[4]
#         for i in range(r1,r2+1):
#             for j in range(c1,c2+1):
#                 if x[0]==1:
#                     board[i][j] -= x[5]
#                 else:
#                     board[i][j] += x[5]
        
#     for x in board:
#         for i in range(len(board[0])):
#             if x[i] > 0:
#                 answer += 1

#     return answer
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.06ms, 10.2MB)
# 테스트 3 〉	통과 (0.57ms, 10.2MB)
# 테스트 4 〉	통과 (1.07ms, 10.4MB)
# 테스트 5 〉	통과 (1.84ms, 10.2MB)
# 테스트 6 〉	통과 (4.27ms, 10.3MB)
# 테스트 7 〉	통과 (7.43ms, 10.2MB)
# 테스트 8 〉	통과 (19.16ms, 10.4MB)
# 테스트 9 〉	통과 (12.85ms, 10.3MB)
# 테스트 10 〉	통과 (26.52ms, 10.3MB)

# O(K * M)
def solution(board, skill):
    for x in skill:
        r1,c1,r2,c2=x[1],x[2],x[3],x[4]
        adition = [0] * len(board[0])
        for j in range(c1,c2+1):
            if x[0]==1:
                adition[j] = -x[5]
            else:
                adition[j] = x[5]
        for i in range(r1,r2+1):
            board[i] = add(board[i],adition)

    return check(board)


def add(a,b):
    for i in range(len(a)):
        a[i]+=b[i]
    return a

def check(board):
    answer = 0
    for x in board:
        for i in range(len(board[0])):
            if x[i] > 0:
                answer += 1
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (0.18ms, 10.2MB)
# 테스트 4 〉	통과 (0.68ms, 10.2MB)
# 테스트 5 〉	통과 (1.14ms, 10.3MB)
# 테스트 6 〉	통과 (3.37ms, 10.3MB)
# 테스트 7 〉	통과 (4.01ms, 10.4MB)
# 테스트 8 〉	통과 (5.86ms, 10.2MB)
# 테스트 9 〉	통과 (7.55ms, 10.3MB)
# 테스트 10 〉	통과 (15.28ms, 10.3MB)