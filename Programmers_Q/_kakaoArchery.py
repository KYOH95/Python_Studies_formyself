"""
양궁대회
link: https://programmers.co.kr/learn/courses/30/lessons/92342?language=python3

"""




answer = [-1]
def BF(k,n,selected,info):
    sum_ = 0
    global answer
    ryan_list = [0 for _ in range(0,11)]
    temp_ryan = 0
    temp_Appeach = 0

    if k == n:
        for x in range(0,11):
            if ryan_list[x]>info[x]:
                temp_ryan += 10-x
            else:
                if info[x] > 0:
                    temp_Appeach += 10-x

        if temp_ryan > sum_ and temp_ryan > temp_Appeach: 
            sum_ = temp_ryan
            answer = ryan_list.copy()
            
    else:
        for point in range(0,11):
            selected[k] = point
            ryan_list[point] += 1
            #여기를 푸시오....
            if ryan_list[point] > info[point]:
                temp_ryan += 10-point

            BF(k+1,n,selected,info)
            ryan_list[point] -= 1

            

def solution(n, info):
    global answer
    
    selected  = [0 for _ in range(n)]
    BF(0,n,selected,info)

    return answer

# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
print(solution(9,[0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(10,[0,0,0,0,0,0,0,0,3,4,3]))