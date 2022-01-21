
def solution(answers):

    list_1 = [1, 2, 3, 4, 5]
    list_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    list_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {id: 0 for id in range(1,4)}

    for i in range(0,len(answers)):
        if answers[i] == list_1[i%5]: count[1] += 1
        if answers[i] == list_2[i%8]: count[2] += 1
        if answers[i] == list_3[i%10]: count[3] += 1

    count_list = sorted(count, key = lambda x: (-count[x],x))

    answer = []
    temp = count[count_list[0]]
    for x in count_list:
        if count[x] == temp:
            answer.append(x)
            temp = count[x]

    return answer

print(solution([1,3,2,4,2]))

print(solution([1,1]))