#나이트 경우의 수

xy = input()

x_list = ['a','b','c','d','e','f','g','h']

x_temp = ord(xy[0:1])
# for i in range(0,x_list):
#     if x_list[i] == x_temp:
#         x = i+1

x = x_temp-96
y = int(xy[1:2])

move_types = ['ULL','URR','DLL','DRR','LUU','RUU','LDD','RDD']
dx = [-1,-1,1,1,-2,-2,2,2]
dy = [-2,2,-2,2,-1,1,-1,1]

count = 0

for i in range(len(move_types)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count +=1
    
print(count)
