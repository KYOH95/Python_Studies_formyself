#9/29/21
#저울문제

#input: 7(추의 갯수)            output: 21
#       3 1 6 2 7 30 1
#       1 1 2 3 6 7 30

N = int(input())

Weight = list(map(int,input().split()))
Weight.sort()

# print(Weight)

Weight_possible = []
