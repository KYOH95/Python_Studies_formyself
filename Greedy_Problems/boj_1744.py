#수 묶기/ NP
# 10/4/21

N = int(input())
numbers_pos = []
numbers_neg = []
for _ in range(N):
    num = int(input())
    if num < 0:
        numbers_neg.append(num)
    else:
        numbers_pos.append(num)

used_p = [0 for _ in range(len(numbers_pos))]
numbers_pos.sort(reverse = True)

if len(numbers_neg)%2==1:
    numbers_neg.append(numbers_pos[len(numbers_pos)-1])
    used_p[len(numbers_pos)-1]=1

used_n = [0 for _ in range(len(numbers_neg))]

# print(numbers)
# print(numbers_neg)
# print(used_p)
# print(used_n)


def calculator(sum,numbers,used):
    for i in range(0,len(used)-1):
        if used[i] == 1:
            continue
        if numbers[i] * numbers[i+1] > numbers[i] + numbers[i+1]:
            sum += numbers[i] * numbers[i+1]
            used[i] = 1
            used[i+1] = 1
        else:
            sum += numbers[i]
            used[i] = 1

    if used[len(used)-1]==0:
        used[len(used)-1]=1
        sum += numbers[len(used)-1]

    return sum


print(calculator(calculator(0,numbers_pos,used_p),numbers_neg,used_n))