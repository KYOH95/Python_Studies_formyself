import heapq
def solution(operations):
    answer = []
    tree = []
    
    for i in operations:
        op = i.split(" ")[0]
        num = int(i.split(" ")[1])
        
        #연산이 I 인지 D인지 확인
        if op == "I":
            heapq.heappush(tree, num)
        else:
            #큐가 비어있으면 연산안함
            if not tree: continue
            elif num == 1:
                heapq._heapify_max(tree)
            elif num == -1:
                heapq.heapify(tree)
            heapq.heappop(tree)
    
    #정답란이 비어있으면
    if not tree:
        return [0,0]
    else:
        heapq._heapify_max(tree)
        answer.append(tree[0])
        heapq.heapify(tree)
        answer.append(tree[0])
    
    return answer