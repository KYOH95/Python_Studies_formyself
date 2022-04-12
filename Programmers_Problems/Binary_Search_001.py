"""
이분탐색 입국심사
link: https://programmers.co.kr/learn/courses/30/lessons/43238
"""

def solution(n, times):
    L = 1
    R = n*times[-1]
    ans = n*times[-1]

    while L <= R:
        mid = (L+R)//2
        cnt = 0
        for t in times:
            cnt += mid // t
        if cnt >= n:
            ans = mid
            R = mid - 1
        else:
            L = mid + 1
    return ans

print(solution(6,[7,10]))
#Return 28
# print(solution(10,[1,3,4,6,10]))
