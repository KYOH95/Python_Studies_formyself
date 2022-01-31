
  

def solution(number, k):
    answer = ''
    
    start_max = int(number[0])
    start_index = 0

    for i in range(0, k+1):
        print("i =",i, "max =", start_max)

        if int(number[i]) > start_max:
            start_max = int(number[i])
            start_index = i
            break

    count = k - start_index
    answer += number[start_index]
    for i in range(start_index+1, len(number)-1):
        if count == 0: 
            mid = i
            break
        if number[i] < number[i+1]:
            count -= 1
        else:
            answer += number[i]

    if count == 0:
        for i in range(mid,len(number)):
            answer += number[i]


    print("hit")
    print(start_max,start_index,count)
    print(answer)
    return answer


solution("4177252841",4)