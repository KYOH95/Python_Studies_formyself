

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
startIndex = 0

sum = land[startIndex]
last = startIndex
for i in range(1,len(land)):
    temp = land[i]
    removeNumber = land[i][last]
    temp.remove(removeNumber)
    print(temp)


print(max([1,2,3,4]))