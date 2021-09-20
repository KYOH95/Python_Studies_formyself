
# N 모험가의 수
# N모험가 각각의 공포도의 값(N이하)

N = int(input())

GP = list(map(int,input().split()))

GP.sort()

result = 0
count = 0

for i in GP:
    count += 1
    if i <= count:
        result += 1
        count = 0

print(result)
