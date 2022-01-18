"""
전화번호 목록

link: https://programmers.co.kr/learn/courses/30/lessons/42577
velog: https://velog.io/@kakasi18/Programmers%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

#### 제한 사항
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.
- 같은 전화번호가 중복해서 들어있지 않습니다.

### 입출력 예제
>phone_book	return
- ["119", "97674223", "1195524421"]	false
- ["123","456","789"]	true
- ["12","123","1235","567","88"]	false

"""

# 효율성 X / for문을 한번만 사용 할 필요가 있음
# def solution(phone_book):
#     phone_book.sort(key = len)

#     for i in range(len(phone_book)-1):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[i]==phone_book[j][:len(phone_book[i])]:
#                 return False

#     return True



def solution(phone_book):
    # phone_book.sort(key = len)
    phone_dic = {}
    
    for nums in phone_book:
        phone_dic[nums] = 1

    for nums in phone_book:
        temp = ''
        for num in nums:
            temp += num
            if temp in phone_dic and temp != nums:
                return False
                
    return True


print(solution(["119", "97674223", "1195524421","120"]))

