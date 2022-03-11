"""
가장큰수
link: https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
"""

move = [[1,0],[0,1],[-1,0],[-1,0]]
count = 0
answer = []
def dfs(x,y,maps,visited,n,m):
	global count
	global answer
	count += 1
	if x == n and y == m:
		answer.append(count)
	else: 
		visited[x][y] = True
		for i in move:
			nx = x+i[0]
			ny = y+i[1]
			if nx < 0 or nx>=len(maps) or ny < 0 or ny>=len(maps[0]): continue
			if visited[nx][ny] == True: continue
			if maps[nx][ny] == 1:
				dfs(nx,ny,maps,visited,n,m)
				# visited[x][y] = False
				count -= 1

def solution(maps):
	global answer
	n = len(maps)-1
	m = len(maps[0])-1
	visited = [[False for _ in range(m+1)] for _ in range(n+1)]
	dfs(0,0,maps,visited,n,m)

	if answer == []:
		answer.append(-1)
	return min(answer)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
