# import sys
# from collections import deque
# sys.setrecursionlimit(100000)
# si = sys.stdin.readline

def solution(n,capacity,files):
    files.sort()
    N = len(files)
    
    # selected = [0 for _ in range(m)]
    # used = [0 for _ in range(n + 1)]
    # def rec_func(k):
    #     if k == m:
    #         for x in selected:
    #             sys.stdout.write(str(x) + ' ')
    #         sys.stdout.write('\n')
    #     else:
    #         start = 1 if k == 0 else selected[k - 1] + 1
    #         for cand in range(start, n + 1):
    #             selected[k] = cand
    #             rec_func(k + 1)
    #             selected[k] = 0

    # selected = []
    # used = [False for _ in range(N)]   
    # cnt = 0 
    # def BF(k,sum,cnt):
    #     start = 1 if k == 0 else selected[k-1] + 1
    #     for i in range(start, N):
    #         if sum + files[i] <= capacity:
    #             selected.append(files[i])
    #             sum += files[i] 
    #             used[i] = False
    #             cnt+=1
    #         else:
                
    #         BF(k+1,sum,cnt)
    #         sum += files[i] 
    #         used[i] = True
    #         cnt-=1

                
    # BF(0,0,0)


    answer = -1
    return answer


print(solution(2,5,[1,2,3,4,5]))