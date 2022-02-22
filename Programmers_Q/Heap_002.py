"""
디스크 컨트롤러
link: https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
"""

import heapq
def solution(jobs):
    heapq.heapify(jobs)
    sec = 0
    answer = 0
    heap = []
    l = len(jobs)

    p_check = False
    p_now = 0    

    while True:
        # print("S:",sec,"p:",p_now)
        if not jobs and not heap and p_check == False: break

        # at some point(sec), push over to heap list from jobs
        while jobs:
            if jobs[0][0] == sec:
                heapq.heappush(heap,jobs[0])
                heapq.heappop(jobs)
            else: break
            if not jobs: break
        
    
        # ask if it is on the processing or not
        if p_check == False:
            p_index = 0
            if len(heap) > 1:
                min = heap[0][1] - heap[0][0]
                for i in range(1,len(heap)):
                    if heap[i][1] - heap[i][0] < min:
                        min = heap[i][1] - heap[i][0]
                        p_index = i
            
            p_now = heap[p_index][1] - heap[p_index][0] - 1
            temp_sec = heap[p_index][0]
            del heap[p_index]
            p_check = True
            

        else: #if processing
            p_now -= 1
        
        sec += 1
        #when processing is done
        if p_now == 0:
            # print(sec, sec - temp_sec)
            answer += sec - temp_sec
            p_check = False
    
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))