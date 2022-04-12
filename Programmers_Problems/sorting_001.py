#K번째 수

def solution(array, commands):
    answer = []

    for x in commands:
        start = x[0] - 1
        end = x[1]
        N = x[2] -1

        arrayB = array[start:end]
        arrayB.sort()
        

        answer.append(arrayB[N])
    
    return answer                                                               


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))