def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(int(100000))]

    #graph
    for fare in fares:
        graph[fare[0]].append([fare[1],fare[2]])       
        graph[fare[1]].append([fare[0],fare[2]])
    
    #BruteForce
    used = [0 for _ in range(int(100000))]
    def search_route(graph, start, end, fare=0):
        if start == end:
            fare_list.append(fare)
        else:
            for node,value in graph[start]:
                if used[node]:
                    continue
                fare += value
                used[node]=1
                search_route(graph, node, end, fare)
                fare -= value
                used[node]=0


    global fare_list
    #start to a
    fare_list = []
    search_route(graph, s, a, fare=0)
    sTOa = min(fare_list)

    #start to b
    fare_list = []
    search_route(graph, s, b, fare=0)
    sTOb = min(fare_list)

    #a to b
    fare_list = []
    search_route(graph, a, b, fare=0)
    aTOb = min(fare_list)
        

    # print("sa: ",sTOa)
    # print("sb: ",sTOb)
    # print("ab: ",aTOb)
    
    return min(aTOb + min(sTOa,sTOb),(sTOa+sTOb))

    
print(solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,	3,	4,	1,	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,	4,	5,	6,	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))