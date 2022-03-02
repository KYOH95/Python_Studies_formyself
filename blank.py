

from numpy import VisibleDeprecationWarning


visited = [True for _ in range(4)]
visited = [False, True, False, True]

print(visited)

if not visited: print("111")
if visited: print("222")
if visited == False: print("333")

if all(visited): print("444")