"""
디스크 컨트롤러
link: https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
"""

import heapq
def solution(jobs):
    sec = -1
    answer = 0
    heapq.heapify(jobs)
    inProcess = []
    l = len(jobs)
    working = False

    while True:        
        #loop out 
        if not jobs and not inProcess and not working : break
        sec += 1

        # at some point(sec), push over to heap list from jobs
        while jobs:
            if jobs[0][0] == sec:
                heapq.heappush(inProcess,[jobs[0][1],jobs[0][0]])
                heapq.heappop(jobs)
            else: break
            # if not jobs: break
		
        #check if the machine is working or not
        if not working: #if not, then start working
            if not inProcess: continue
            p_cnt = inProcess[0][0] - 1
            p_start = inProcess[0][1] -1
            heapq.heappop(inProcess)
            working = True
        else: p_cnt -= 1 #if working, then keep working
            
        #check if working is done. if yes, +answer then, make 'working' back to False
        if p_cnt == 0:
            answer += sec - p_start
            working = False

    return answer//l

print(solution([[0, 3], [10, 3], [2, 4]]))
print(solution([[0, 1], [1, 1], [3, 1], [2,6],[50, 7]]))

