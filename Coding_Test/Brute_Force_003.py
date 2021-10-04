
#BOJ 15652

N,M = map(int,input().split())

selected = [0 for _ in range(M)]


def rec_fucn(k):
    if k == M:
        for x in selected:
            print(x,end=' ')
        print()
    else:
        if k == 0: start = 1
        else: start = selected[k-1]
        for cand in range(start,N+1):
            selected[k] = cand
            rec_fucn(k+1)
            

rec_fucn(0)