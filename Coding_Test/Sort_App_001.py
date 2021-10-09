#BOJ_10825
#10/8/21
#국영수 문제

N = int(input())
S = []

for i in range(N):
    temp = input().split()
    temp[1:] = map(int, temp[1:])
    S.append(temp)

S.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))


for x in S:
    print(x[0])