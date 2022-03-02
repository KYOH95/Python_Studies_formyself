answer = []
def DFS(graph,visited,start,sum_):
	global answer
	visited[start] = True
	if all(visited):
		answer.append(sum_)
	else:
		for i in graph[start]:
			if visited[i[0]] == False:
				sum_ += i[1]
				DFS(graph,visited,i[0],sum_)
				sum_ -= i[1]
				visited[i[0]] = False

def solution(n, costs):
	global answer
	graph = [[] for _ in range(n)]
	for i in range(len(costs)):
		graph[costs[i][0]].append([costs[i][1],costs[i][2]])
		graph[costs[i][1]].append([costs[i][0],costs[i][2]])
	print(graph)
	
	for i in range(n):
		visited = [False for _ in range(n)]
		DFS(graph,visited,i,0)
		print(answer)
	print(min(answer))
	return min(answer)

# solution(5,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8],[4,0,2]])
# solution(5,[[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]])
# solution(4,[[0,1,1],[0,2,2],[2,3,1]])
solution(6,[[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])