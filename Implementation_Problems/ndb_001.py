# 9/19/2021
#상하좌우 

#동북서남

# dx = [0,1,0,-1]
# dy = [1,0,-1,0]

# x,y = 2,2

# for i in range(0,4):
#     nx = x+dx[i]
#     ny = y+dy[i]
#     print(nx,ny)


#------------------------------------

# N = int(input())

# move = input().split()

# #     L R U D
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types = ['L','R','U','D']

# x,y = 1,1

# for j in move:
#     for i in range(len(move_types)):
#         if j == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]

#     if nx < 1 or ny < 1 or nx > N or ny > N:
#         continue

#     x,y = nx, ny
#     print(x,y)

# # print(x,y)


#------------------------------------------
#연습

N = int(input())

plan = input().split()

move_types = ['R','L','U','D']
dx = [0,0,-1,1]
dy = [1,-1,0,0]

x,y = 1,1

for i in plan:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x,y = nx,ny

print(x,y)