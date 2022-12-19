# lv.1 
#2022 KAKAO TECH INTERNSHIP
#성격 유형 검사하기


def solution(survey, choices):
    answer = ''
    
    dict_char = {"R":0,"T":0,"C":0,"F":0,
                "J":0,"M":0,"A":0,"N":0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            dict_char[survey[i][0]] += 4-choices[i]
        else:
            dict_char[survey[i][1]] += choices[i]-4
    
    if dict_char["R"] >= dict_char["T"]: answer += "R"
    else: answer += "T"
    if dict_char["C"] >= dict_char["F"]: answer += "C"
    else: answer += "F"
    if dict_char["J"] >= dict_char["M"]: answer += "J"
    else: answer += "M"
    if dict_char["A"] >= dict_char["N"]: answer += "A"
    else: answer += "N"
    
    return answer