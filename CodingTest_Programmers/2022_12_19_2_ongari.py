# 옹알이 lv.1

def solution(babbling):
    answer = 0
    dict_ = {"aya":"1","ye":"2","woo":"3","ma":"4"}
    
    for i in babbling:
        for k,v in dict_.items():
            i = i.replace(k,v)
        
        if i.isnumeric(): 
            continuous = False
            for idx in range(len(i)-1):
                if i[idx] == i[idx+1]:
                    continuous = True
                    break
            
            if not continuous: answer += 1
                
    return answer