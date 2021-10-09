#15663 N과M(9)

#input: 3 1
#       4 4 2

N, M = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()

selected = [0 for _ in range(M)]
used = [0 for _ in range(N+1)]



def rec_func(k):
    if k == M:
        for x in selected:
            print(x,end = " ")
        print()
        
    else:
        last_cand = 0
        for cand in range(N):
            if used[cand] == 1 or last_cand == numbers[cand]:
                continue
            else:
                last_cand = numbers[cand]
                selected[k] = numbers[cand]
                used[cand] = 1
                rec_func(k+1)
                selected[k] = 0
                used[cand] = 0


rec_func(0)
