#회의실 배정
#input: 11              output:4
#       1 4
#       3 5
#       ...

N = int(input())
lecture_list = []

for _ in range(N):
    lecture_list.append(list(map(int,input().split())))


lecture_list.sort(reverse=True)
print(lecture_list)

# count = 1
# for i in range(1,len(lecture_list)-1):
#     for j in range(i+1,len(lecture_list)):

count = 0
