# 9/29/21  Passed!
# 신입사원 문제 / 두가지 심사중에 두부분이 모두 어떤 다른 지원자보다 순위가 뒤로 밀려있으면 뽑지 않는다. 
# 예) 5 5 지원자는 다른 어떠한 3 2 지원자보다 두분에서 부족하기 때문에 대상에서 제거 된다.

# input:2 (how many tests)         output: 4
#       5 (how many cases)                 3
#       3 2
#       1 4
#       4 1
#       2 3
#       5 5

#       7 (how many cases)                 
#       3 6
#       7 3
#       4 2
#       1 4
#       5 7
#       2 5
#       6 1


Test = int(input())
ans = []
def function_interview():
    Case = int(input())
    test_list = []
    for i in range(Case):
        test_list.append(list(map(int,input().split())))

    count = 0
    for i in range(0,len(test_list)):
        for j in range(0,len(test_list)):
            if i==j:
                continue
            if test_list[i][0] > test_list[j][0]:
                if test_list[i][1] > test_list[j][1]:
                    count +=1
                    break

    ans.append(Case-count)


for i in range(Test):
    function_interview()

print(ans)