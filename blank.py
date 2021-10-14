#practice
import sys
si = sys.stdin.readline

# T = int(si())
M,N,K = map(int,si().split())
K_list = [[0]*M for _ in range(N)]

# for _ in range(K):
#     a,b = map(int,si().split())
#     K_list[a][b] = 1

for i in range(N):
    for j in range(M):
        print(K_list[i][j],end='')
    print()