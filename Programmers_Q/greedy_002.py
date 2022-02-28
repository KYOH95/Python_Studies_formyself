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

# 1. 오른쪽으로만 가면서 체크해보기
def right(check):
    d = 0
    for i in range(len(check)):
        if check[i] == False: d = i
    return d

# 2. 왼쪽으로만 가면서 체크해보기
def left(check):
    d = 0
    for i in range(len(check)-1,0,-1):
        if check[i] == False: d = len(check)-i
    return d

# 3. 오른쪽으로 절반 갔다가 왼쪽으로 가서 체크해보기
def rightLeft(check):
    d,temp = 0,0
    for i in range(0,len(check)//2):
        if check[i] == False: d = i*2
    for i in range(len(check)-1,(len(check)//2)-1,-1):
        if check[i] == False: temp = len(check)-i
    return d + temp

# 4. 왼쪽으로 절반 갔다가 오른쪽으로 가서 체크해보기
def leftRight(check):
    d,temp = 0,0
    for i in range(len(check)-1,(len(check)//2),-1):
        if check[i] == False: d = (len(check)-i) * 2
    for i in range(0,(len(check)//2)+1):
        if check[i] == False: temp = i
    return d + temp

def solution(name):
    answer = 0
    check = [False for _ in range(len(name))]
    # Bool 체크리스트 만들기 | 만약 "A"면 True
    for i in range(0,len(check)):
        if i == 0: check[i] = True
        if name[i] == 'A':
            check[i] = True
    
    #최소 좌우이동 갯수 계산 4가지 방법
    r = right(check)
    l = left(check)
    rl = rightLeft(check)
    lr = leftRight(check)
    answer = min(r, l, rl, lr)
    
    #알파벳 상하로 움직이기 계산
    for x in name:
        up = ord(x)-ord('A')
        down = 1 + ord('Z')-ord(x)
        answer += min(up,down)
        
    return answer

# print(solution("JAAON"))
# print(solution("JAN"))
print(solution("AAABBAAAABBAAAAAAA"))
