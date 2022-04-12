"""
link: https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
velog: https://velog.io/@kakasi18/Programmers%EC%8B%A0%EA%B7%9C-%EC%95%84%EB%94%94%EB%94%94-%EC%B6%94%EC%B2%9C


1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

"""


def solution(new_id):
    answer = list(new_id)
    #1
    for i in range(len(answer)):
        if ord(answer[i]) >= 65 and ord(answer[i]) <= 90: 
            answer[i] = chr(ord(answer[i])+32)
    
    #2
    remove_ = []
    for i in range(len(answer)):
        # 알파벳 소문자
        if ord(answer[i]) >= 97 and ord(answer[i]) <= 122: pass 
        # 숫자
        elif ord(answer[i]) >= 48 and ord(answer[i]) <= 57: pass
        # 빼기, 밑줄, 마침표
        elif ord(answer[i]) == 95 or ord(answer[i]) == 45 or ord(answer[i]) == 46 : pass 
        else:        
            remove_.append(answer[i])
    
    for x in remove_:
        answer.remove(x)

    #3
    Bool_ = False
    count = 0
    for i in range(len(answer)):
        if Bool_ == False:
            if answer[i] == '.':
                Bool_ = True 
        else:
            if answer[i] == '.':
                answer[i] = '*'
                count += 1
            else:
                Bool_ = False

    for i in range(count):
        answer.remove('*')

    #4
    if len(answer)>0:
        if answer[len(answer)-1] == '.':
            answer.pop(len(answer)-1)
    if len(answer)>0:
        if answer[0]=='.':
            answer.pop(0)
    
    #5
    if len(answer)==0:
        answer.append('a')

    #6
    if len(answer) >= 16:
        temp = []
        for i in range(0,15):
            temp.append(answer[i])
        answer = temp
        
        if answer[len(answer)-1] == '.':
            answer.pop(len(answer)-1)


    #7
    while len(answer) < 3:
        answer.append(answer[len(answer)-1])

    #convert
    a_string = "".join(answer)
        
    return a_string


newid = "...!@BaT#*..y.abcdefghijklm"
print(solution(newid))