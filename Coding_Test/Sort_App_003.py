#boj_11652
#카드

N = int(input())
card = []

for i in range(N):
    card.append(int(input()))


card.sort()

ans = card[0]
count = 1
max = 1

for i in range(1,N):
    if card[i] == card[i-1]:
        count += 1
    else:
        count = 1
    if max < count:
        max = count
        ans = card[i]
    # C_list[i] = card[i],count

print(ans)
