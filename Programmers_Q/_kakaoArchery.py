"""
양궁대회
link: https://programmers.co.kr/learn/courses/30/lessons/92342?language=python3

"""



def solution(n, info):
    
    max_ = 0
    answer = [-1]
    sum_ryan = 0
    sum_appeach = 0
    for i in range(0,11):
        if info[i] > 0: 
            sum_appeach += 10-i

    selected  = [0 for _ in range(n)]
    counted_check = [0 for _ in range(11)]


    def BF(k,n,selected,info):        
        #5번째 화살까지 쏘면
        if k == n:
            if selected[0]==0 and selected[1]==0 and selected[2]==0:
                print(selected)
            
        else:
            for point in range(0,11):
                selected[k] = point
                # if counted[]
                
                if selected.count(point) <= info[point]+1:
                    BF(k+1,n,selected,info)
                else:
                    pass
    
    BF(0,n,selected,info)
    
    return answer

# print(solution(1,[0,1,0,0,0,0,0,0,0,0,0]))
print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))