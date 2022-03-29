"""
공유기 설치
link: https://www.acmicpc.net/problem/2110
"""

import sys
si = sys.stdin.readline
N,C = list(map(int,si().split()))

house = [0 for _ in range(N)]
for i in range(N):
    house[i] = int(si())
house.sort()

#입력받은 거리를 최대로 C개의 공유기 설치가능 여부 확인
def check(distance):
    count = 1
    last = house[0]
    for i in range(1,N):
        if house[i] - last < distance: continue
        last = house[i]
        count += 1
    return count >= C

#가장 적합한 거리 구하기
def bs(L,R):
    result = R+1
    while L <= R:
        mid = (L+R)//2
        if check(mid):
            result = mid
            L = mid + 1
        else:
            R = mid - 1
    return result

print(bs(0,house[-1]))
