
# 보석 N개: M무게 & V가격
# 가방 K개: 각 C무게

# input: N K

N, K = map(int,input().split())

#각 N개 줄에는 보석 정보 M / V

data = dict()

for _ in range(N):
    a,b = map(int,input().split())
    data[a] = b


# 각 K개 줄에는 무게 C 입력
bags = []
for _ in range(K):
    bags.append(int(input()))

bags.sort()

key_list = data.keys()
# value_list = data.values()

sum = 0

for i in bags:
    temp = 0
    for j in key_list:
        if j <= i and data[j] >= temp:
            temp = data[j]
            key = j
        
    sum += temp
    del data[key]


print(sum)
