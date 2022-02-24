
import heapq

# list = [[0, 5], [2, 3], [1, 2], [9,4], [8,10]]
list = []
heapq.heappush(list,7)
heapq.heappush(list,5)
heapq.heappush(list,-5)


print(list)
heapq._heapify_max(list)
heapq._heappop_max(list)

print(list)

