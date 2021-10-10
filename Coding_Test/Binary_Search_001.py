#boj_7795
#먹을것인가 먹힐것인가

def binary_search(list_B,x,L,R):
    result = -1
    while L <= R:
        M = (L+R)//2
        if list_B[M] < x:
            L = M+1
            result = M
        else:
            R = M-1
    return result
        

def solve():
    B.sort()
    ans = 0
    for x in A:
        ans += binary_search(B,x,0,M-1) + 1
    print(ans)

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    solve()
    

