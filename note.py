
# Note


#-----------------------------------------------------------------

[1] #Slicing
# Index: list[0,1,2,3,4]
# Index: list[-4,-3,-2,-1]
# list[-1] = 리스트 마지막에 있는 자료

# delete: list[:-1] 마지막 하나 제거
# reverse: list[::-1] step을 거꾸로 하나씩 해서 처음부터 끝까지 돌려라
#           [ 시작 : 끝 : 스텝]

#-----------------------------------------------------------------

[2] #Sort

# list.sort(key = lambda x:(x[1],-x[2]))
#                           1번째 우선순위 x[1]에 대하여 오름차순
#                           2번째 우선순위 x[2]에 대하여 내림차순 
#                       
#-----------------------------------------------------------------

[3] #input
import sys
si = sys.stdin.readline
A = si()
B = si()
print(A,end='')
print(B)