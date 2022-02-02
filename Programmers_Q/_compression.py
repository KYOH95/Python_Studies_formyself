

def check(s,len_):
    end = len(s) - (len(s)%len_)
    temp = ''
    current = ''
    count = 0
    answer = ''
    for i in range(0,end):
        if i % len_ == 0:
            if temp != current:
                if count > 1:
                    answer += str(count)
                answer += (temp)
                temp = current
                count = 1
            else:
                count += 1
            current = ''

        current += s[i]

        if i == end-1:
            if temp == current:
                count += 1
                answer += str(count)
                answer += temp
            else:
                if count > 1:
                    answer += str(count)
                answer += temp
                answer += current
    
    for i in range(end,len(s)):
        answer += s[i]

    return len(answer)


def solution(s):
    answer = len(s)
    max = len(s)//2
    for i in range(1,max+1):
        temp = check(s,i)
        if temp < answer:
            answer = temp
    return answer



solution("aabbaccc")
solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
