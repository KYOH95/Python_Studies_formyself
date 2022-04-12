count_delete = 0
count_rotate = 0
#새로운 이진법을 구하는 함수
def getNewString(s):
    global count_delete
    global count_rotate

    temp = len(s)
    #'0' 제거하기
    for x in s:
        if x == '0':
            count_delete += 1
            temp -= 1
    
    newString = ''
    #제거하고 남은 길이를 2진법으로 바꾸기
    while True:
        newString = str(temp % 2) + newString
        temp = temp // 2
        if temp == 0: 
            break
    
    return newString
        
#메인함수
def solution(s):
    answer = []
    global count_delete
    global count_rotate
    
    #2진법으로 바꿔진 string이 '1'이 될때까지 반복문 진행
    while True:
        s = getNewString(s)
        count_rotate += 1
        if s == '1': break

    answer.append(count_rotate)
    answer.append(count_delete)
    return answer

print(solution("110010101001"))
# print(solution("01110"))
# print(solution("1111111"))
