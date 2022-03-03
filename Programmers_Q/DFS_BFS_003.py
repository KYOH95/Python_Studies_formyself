"""
단어 변환
link: https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
"""

count = 0
answer = []
def DFS(start, target, words, used):
    global count
    global answer
    if start == target:
        answer.append(count)
    else:
        for cand in words:
            diff = 0
            for i in range(len(cand)):
                if start[i]!= cand[i]:
                    diff += 1
                if diff >= 2: break
            if diff == 1 and cand not in used:
                count +=1 
                used.append(cand)
                DFS(cand,target,words, used)
                used.pop()
                count -=1

def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    
    used = []
    DFS(begin, target, words, used)
    return min(answer)

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
