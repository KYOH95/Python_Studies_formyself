"""
양궁대회
link: https://programmers.co.kr/learn/courses/30/lessons/92342?language=python3

"""



sum_ = 0
answer = [-1]
def BF(k,n,selected,info):
    global sum_ 
    global answer
    # global ryan_list
    sum_ryan = 0
    sum_appeach = 0
    counted = []

    if k == n:
        # ryan_list = [0 for _ in range(0,11)]
        # for x in selected:
        #     ryan_list[x] += 1
        
        for i in range(0,10):
            if selected.count(i) > info[i]:
                sum_ryan += 10-i
            else:
                if info[i]>0:
                    sum_appeach += 10-i

        if sum_ryan > sum_ and sum_ryan > sum_appeach: 
            sum_ = sum_ryan
            answer = selected.copy()
            
    else:
        for point in range(0,11):
            selected[k] = point
            
            if selected.count(point) <= info[point]+1:
                BF(k+1,n,selected,info)


def solution(n, info):
    global answer
    
    selected  = [0 for _ in range(n)]
    BF(0,n,selected,info)
    
    return answer

# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))