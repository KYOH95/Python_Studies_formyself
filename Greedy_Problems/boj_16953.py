#9/29/21  Passed
#A -> B

#두가지 연산만 가능하다
# 1) 2를 곱한다
# 2) 1을 수의 오른쪽에 붙인다. 예) 8 -> 81

#A가 B로 변할때의 최솟값을 구하라

#input: 2 162           output: 5
#       4 42                    -1
#       100 40021               5


A, B = map(int,input().split())


count = 1
while True:
    if A == B:
        print(count)
        break
    elif (B % 10 != 1 and B % 2 == 1) or A > B:
        print(-1)
        break
    elif B % 10 == 1:
        B = (B-1) // 10
        count += 1 
    else:
        B = B // 2
        count += 1
