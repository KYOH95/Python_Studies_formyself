# 9/19/2021
#완전 탐색 !

#3이 하나라도 들어가면 세어야 하는 문제

count = 0

hour_ = int(input())
min_ = 60
sec_ = 60

#0-59초 사이에 몇개 인가
for h in range(0,hour_+1):
    for j in range(0,min_):
        for i in range(0,sec_):
            if '3' in str(h)+str(j)+str(i):
                count+=1


print(count)

#-------------------------------------
