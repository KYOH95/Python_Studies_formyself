def solution(n):
    answer = 1
    
    sum = 0
    left = 1
    right = 1
    while left < (n//2)+1:
        if sum < n:
            sum += right
            right += 1
        else:
            if sum == n: 
                answer += 1
                print(left,right)
            sum -= left 
            left += 1
        
    
    return answer

print(solution(15))