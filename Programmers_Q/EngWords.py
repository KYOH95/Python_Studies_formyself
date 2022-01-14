
"""
link: https://programmers.co.kr/learn/courses/30/lessons/81301
velog: https://velog.io/@kakasi18/Programmers%EC%88%AB%EC%9E%90-%EB%AC%B8%EC%9E%90%EC%97%B4%EA%B3%BC-%EC%98%81%EB%8B%A8%EC%96%B4

네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine
제한사항
1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.
입출력 예
s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123

"three"는 3, "six"는 6, "seven"은 7에 대응되기 때문에 정답은 입출력 예 #2와 같은 234567이 됩니다.
입출력 예 #2와 #3과 같이 같은 정답을 가리키는 문자열이 여러 가지가 나올 수 있습니다.
입출력 예 #4

s에는 영단어로 바뀐 부분이 없습니다.

"""



def solution(s):
    engList = ['zero','one','two','three','four','five','six','seven','eight','nine']
    temp = list(s)
    answer = []
    words = []

    for x in temp:
        if 48 <= ord(x) <= 57:
            answer.append(x)
        else:
            words.append(x)
            temp_words = ''.join(words)
            for i in range(10):
                if temp_words == engList[i]:
                    answer.append(str(i))
                    words = []

    answer = "".join(answer)
    return int(answer)


s = "one4seveneightnine"

print(solution(s))