
import sys
si = sys.stdin.readline

N,M = list(map(int,si().split()))
lab = [list(map(int,si().split())) for _ in range(N)]

blank = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

print(blank)