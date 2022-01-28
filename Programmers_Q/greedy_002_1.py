"""
*조이스틱*
link: 

[문제 설명]
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

[제한 사항]
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
"JEROEN"	56
"JAN"	23
"""

def check(alpha):
    if ord(alpha)-ord('A') <= ord('Z') - ord(alpha) + 1:
        return ord(alpha) - ord('A')
    else:
        return ord('Z') - ord(alpha) + 1

def solution(name):
    answer = 0 #양옆으로 움직일 수 있는 최대치
    
    for x in name:
        #각각의 알파벳이 최소한으로 변환될 수 있는 횟수를 반환하여 저장
        answer += check(x)
        
    left = 0
    right = 0
    middle = 0
    middleIndex = 0
    middleStart = 0
    middleIndexR = 0
    middleEnd = 0
    #좌,우에 'A'알파벳이 연속적으로 존재하는지 확인. 
    for l in range(1,len(name)):
        if name[l] != 'A': 
            middleIndex = l
            break
        else: left += 1

    for r in range(len(name)-1,0,-1):
        if name[r] != 'A': 
            middleIndexR = r
            break
        else: right += 1
    
    boolCheck = False
    for m in range(middleIndex+1,middleIndexR-1):
        if name[m] == 'A':
            middleStart = m
            boolCheck = True
            while True:
                middle += 1
                m += 1
                if m > middleIndexR -1: 
                    middleEnd = m-1
                    break
                if name[m] != 'A': 
                    middleEnd = m-1
                    break
            break

    middleCount = 0

    if middleStart - 1 < len(name) -1 - middleEnd:
        middleCount = (middleStart-1)*2 + len(name) -1 - middleEnd
    else:
        middleCount = (middleStart-1) + (len(name) -1 - middleEnd)*2
    
    leftCount = len(name)-1 -left
    rightCount = len(name)-1 -right
    
    if boolCheck:
        answer += min(leftCount,rightCount,middleCount)
    else:
        answer += min(leftCount,rightCount)
    return answer  

# print(solution("JAN"))
print(solution("ABAAB"))


# abcdefghijklmnopqrstuvwxyz