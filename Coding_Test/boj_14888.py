#연산자 끼워넣기

N = int(input())
numbers = list(map(int,input().split()))
operator = list(map(int,input().split()))
min = 1e9
max = -1e9

def calculator(number1,operator,number2):
    if operator == 0:
        return number1 + number2
    elif operator == 1:
        return number1 - number2
    elif operator == 2:
        return number1 * number2
    else:
        if number1 < 0:
            return (abs(number1)//number2) * -1
        else:
            return number1 // number2

def rec_fucn(k,value):
    if k == N-1:
        global min,max
        if value <= min:
            min = value
        if value >= max:
            max = value

    else:
        global operator
        for cand in range(4):
            if operator[cand] >= 1:
                operator[cand] -= 1
                rec_fucn(k+1,calculator(value,cand,numbers[k+1]))
                operator[cand] += 1


rec_fucn(0,numbers[0])

print(max)
print(min)