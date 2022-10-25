
def solution(board, moves):
    answer = 0
    # board 90도 회전
    stack=list(zip(*board[::-1]))
    for i in range(len(stack)):
        stack[i] = list(stack[i])

    #moves
    bin = []
    for move in moves:
        move -= 1
        #뽑기
        while True:
            if not stack[move]: break
            elif stack[move][-1]==0:
                stack[move].pop()
            else:
                bin.append(stack[move].pop())
                break
        #터트리기
        while len(bin)>=2:
            if bin[-1]==bin[-2]:
                bin.pop()
                bin.pop()
                answer += 2
            else:break

    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])