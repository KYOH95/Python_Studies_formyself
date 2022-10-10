def solution(s):
    answer = ''
    word_list = " ".join(map(str, s.split(" ")))
    
    for i in range(len(word_list)):
        # if 
        if word_list[i].isupper(): 
            answer += word_list[i].lower()
        else:
            answer += word_list[i]

    return answer


print(solution("3people unFollowed me"))