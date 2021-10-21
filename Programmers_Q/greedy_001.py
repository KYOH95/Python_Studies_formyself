
def check_mine(lost,reserve):
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                del lost[i]
                del lost[j]

def func_(lost,reserve):
    count = 0
    for x in lost:
        for i in range(len(reserve)):
            if x-1 == reserve[i]:
                del reserve[i]
                count += 1
                break
            if x+1 == reserve[i]:
                del reserve[i]
                count += 1
                break
    return count

def solution(n, lost, reserve):
    check_mine(lost,reserve)
    answer = n-len(lost)
    answer += func_(lost,reserve)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(	5, [2, 4], [3]))
print(solution( 3, [3], [1]))