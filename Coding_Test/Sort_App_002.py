#boj_1015
#수열 정렬

# 배열 A에 해당하는 원소들을 수열 P를 통해 정렬된 B를 만든다
# 수열 P를 출력하라

# input: 3(N)       output: 1 2 0
#       2 3 1

N = int(input())
A = list(map(int,input().split()))
B = [0 for _ in range(N)]

for i in range(N):
    B[i] = i,A[i]

B.sort(key = lambda x:x[1])


P = [0 for _ in range(N)]
for i in range(N):
    P[B[i][0]] = i

for x in P:
    print(x,end=" ")
