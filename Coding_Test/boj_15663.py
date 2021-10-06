#15663 N과M(9)

#input: 3 1
#       4 4 2

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()

selected = [0 for _ in range(M)]
used = [0 for _ in range(N)]
check_list = []

def check_(x):
    return x in check_list

def rec_func(k):
    if k == M:
        temp_str = [selected[0]]
        for i in range(1,len(selected)):
            temp_str.append(selected[i])
        
        if check_(temp_str) == False:
            for x in temp_str:
                print(x,end='')
            print()

        check_list.append(temp_str)
        
    else:
        for cand in range(N):
            if used[cand]:
                continue
            else:
                selected[k] = numbers[cand]
                used[cand] = 1
                rec_func(k+1)
                selected[k] = 0
                used[cand] = 0


rec_func(0)
