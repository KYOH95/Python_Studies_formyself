#boj_1920
#수찾기

N = int(input())
N_list = list(map(int,input().split()))
M = int(input())
M_list = list(map(int,input().split()))
N_list.sort()

def binary_func(list,x,L,R):
    while L <= R:
        M = (L+R)//2
        if list[M] == x: return 1
        elif x < list[M]:
            R = M-1
        else:
            L = M+1
    return 0

for x in M_list:
    print(binary_func(N_list,x,0,N-1))
