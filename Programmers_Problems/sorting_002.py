#가장큰수

def solution(numbers):
    # numbers.sort(key=lambda x:-x%(10**(int(len(str(x))))))

    for i in range(1,len(numbers)):
        if numbers[i]%(10**(int(len(str(numbers[i]))))) == numbers[i-1]%(10**(int(len(str(numbers[i-1]))))):
            pass

    answer = ''
    for x in numbers:
        answer += str(x)
    return answer

print(solution([3, 30, 34, 91, 9]))