def solution(numbers, target):
    signs = [1,-1]
    answer_list = []
    
    def dfs(k, sum=0):
        if k == len(numbers):
            if sum == target:
                answer_list.append(1)
        else:
            for sign in signs:
                sum += numbers[k]*sign
                dfs(k+1, sum)
                sum -= numbers[k]*sign
    
    dfs(0,sum=0)
    
    return len(answer_list)