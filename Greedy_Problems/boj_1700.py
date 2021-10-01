#sep.9.21
#멀티탭 스케줄링

# input: 2(멀티탭갯수) 7(사용순서)                output:2
#        2 3 2 3 1 2 7


N, M = map(int,input().split())

M_list = list(map(int,input().split()))
current_list = []



# for i in range(0,M):
#     if M_list[i] == 