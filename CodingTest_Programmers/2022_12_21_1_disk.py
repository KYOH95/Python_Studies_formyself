import heapq
def solution(jobs):
    answer, ms = 0, -1
    length = len(jobs)
    working = False
    requested = []
    heapq.heapify(jobs)
    end = -1

    while True:
        if not jobs and not requested and not working: break
        ms += 1

        #각 해당 시간에 할당 가능 job을 requested에 할당(heappush)
        while jobs:
            if jobs[0][0] == ms:
                heapq.heappush(requested,[jobs[0][1],jobs[0][0]])
                heapq.heappop(jobs)
            else: break
        
        #일하고 있는 중인지, 일이 완료되는 시점인지 확인
        if working and ms == end:
            working = False
        
        #일하지 않는 중이면, 일 할당
        if not working:
            if not requested: continue
            temp = heapq.heappop(requested)
            end = ms + temp[0]
            start = temp[1]
            answer += end - start
            working = True
            
        
    return answer//length
print(solution([[0, 3], [1, 9], [2, 6]]))