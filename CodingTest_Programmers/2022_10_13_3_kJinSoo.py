def solution(n, k):
    answer = 0
    rev_base = ''
    
    #get k진수 list
    while n > 0:
        n, mod = divmod(n, k) #(몫,나머지)
        rev_base += str(mod)
    n_base_k = rev_base[::-1].split("0")
    
    def isPrime(num):
        if num <= 1: return False
        for div in range(2,int(num**(1/2)+1)):
            if num%div==0 and num!=div:
                return False
        return True

    for i in n_base_k:
        if i == "": continue
        if isPrime(int(i)): answer+=1
        
    return answer

          
print(solution(110011,10))