import time

#1
emptylist = [0] * 1000000
start = time.time() 
for i in range(len(emptylist)):
    emptylist.pop()

print("#1 time :", time.time() - start)

#2
emptylist = [0] * 1000000
start = time.time() 
for i in range(len(emptylist)):
    emptylist.pop(0)

print("#2 time :", time.time() - start)