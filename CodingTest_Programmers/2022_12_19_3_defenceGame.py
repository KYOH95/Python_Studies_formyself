from heapq import heappush,heappushpop

def solution(n,k,enemy):
    heap = []
    total = 0
    answer = 0

    for i in enemy:
        total += i
        if total <= n:
            heappush(heap, -i)
            answer += 1
            
        elif k > 0:
            k -= 1
            total += heappushpop(heap, -i)
            answer += 1
        
        print(heap)
    return answer



            


print(solution(7,3,[4,2,4,5,3,3,1]))