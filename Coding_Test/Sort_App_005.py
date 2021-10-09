#20291
#파일 정리

N = int(input())
b = [0 for _ in range(N)]

for i in range(N):
    a, b[i] = input().split(".")

b.sort()
name = []
num = []
count = 1

for i in range(1,N):
    if b[i] == b[i-1]:
        count += 1
    else:
        name.append(b[i-1])
        num.append(count)
        count =1

    if i == N-1:
        name.append(b[i])
        num.append(count)
        break

for i in range(len(name)):
    print(name[i],num[i])

