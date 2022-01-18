"""

link: https://programmers.co.kr/learn/courses/30/lessons/42577


"""


def solution(phone_book):
    phone_book.sort(key = len)

    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                return False

    return True

solution(["119", "97674223", "1195524421","120"])