#완전 탐색 #중복까지 검색
#7^7 = 82만  > 1초에 연산 가능
#boj_15651  N 과 M 


N,M = map(int,input().split())

selected = [0 for _ in range(M)]

def rec_func(k):
    if k==M: #selected 리스트에 모든 수를 다 골랐다면 append()
        for x in selected:
            print(x,end=' ')
        print()
    else:
        #pass #selected[k]의 모든 원소들 
        for cand in range(1,N+1):
            selected[k] = cand
            rec_func(k+1)
            # selected[k] = 0


rec_func(0)