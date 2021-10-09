#A와 B

#input: B           output:
#       ABBA

# S를 T로 바꿀 수 있으면 1, 없으면 0

S = input()
T = input()

#문자열 뒤에 A를 추가
#문자열을 뒤집고 뒤에 B를 추가

while True:
    if len(S) == len(T):
        if S == T: print(1)
        else: print(0)
        break
    if T[-1]== 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

#slicing [::1]
#  start: end : step