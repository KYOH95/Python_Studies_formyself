
#소수를 구하는 함수
def getPrime(number):
    if number <2: return False
    if number == 2: return True
    end = round(number**0.5)
    for i in range(3,end+1):
        if number % i == 0: 
            return False
    return True
        

def solution(n,k):
    answer = 0
    kNumber = ''
    
    #K진수로 변환하는 루프: 몫이 0이 될때까지 숫자를 K진수로 나눈 나머지를 구해서 정답에 적어준 후 몫을 또 K로 나누어준다. 
    while n > 0:
        kNumber = str(n%k) + kNumber
        n = n//k
    
    #'0'을 기준으로 정답을 나누어주고 나누어진 수들을 리스트에 저장한다.
    k_list = kNumber.split('0')
    for x in k_list: #저장된 리스트에 숫자들이 소수인지 판별, 만약 비어있다면 판별하지 않고 넘어간다.
        if x == '': continue
        if getPrime(int(x)):
            answer += 1
    
    return answer
    
print(solution(437674,3))
print(solution(0,10))

    
    


