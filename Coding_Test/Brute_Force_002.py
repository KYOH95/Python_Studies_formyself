#완전탐색 난이도:2
#중복x

#15649번 문제

#input: 3 3

N, M = map(int,input().split())

selected = [0 for _ in range(M)]
used = [0 for _ in range(N+1)]

def rec_fucn(k):
    if k == M:
        for x in selected:
            print(x,end='')
        print()
    else:
        for cand in range(1,N+1):
            if used[cand]:
                continue
            selected[k] = cand
            used[cand] = 1
            rec_fucn(k+1)
            selected[k] = 0
            used[cand] = 0


rec_fucn(0)