def solution(n):
    n_2 = 0
    n_1 = 1
    
    for i in range(n-1):
        current = n_2+n_1
        #update
        n_2 = n_1
        n_1 = current        
        
    return current%1234567