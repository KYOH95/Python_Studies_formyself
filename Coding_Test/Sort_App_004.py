#boj_15970
#화살표 그리기

#input: N                   output: 13(최단거리들의 합)
#       X(좌표) Y(색상)

N = int(input())
point = []

for i in range(N):
    point.append(list(map(int,input().split())))

point.sort(key=lambda x:(x[1],x[0]))

# print(point)

sum = point[1][0] - point[0][0] + point[-1][0] - point[-2][0]
for i in range(1,N-1):
    if point[i][1]-point[i-1][1] == 0 and point[i+1][1]-point[i][1] == 0:
        if point[i][0] - point[i-1][0] < point[i+1][0]-point[i][0]:
            sum += point[i][0] - point[i-1][0]
        else:
            sum += point[i+1][0] - point[i][0]
    elif point[i-1][1] == point[i][1]:
        sum += point[i][0] - point[i-1][0]
    else:
        sum += point[i+1][0] - point[i][0]
        

print(sum)