"""
2개 이하로 다른 비트
link: https://programmers.co.kr/learn/courses/30/lessons/77885?language=python3
"""
	

def solution(s):
	answer = []
	for x in s:
		x_B = bin(int(x))[2:]
		next = int(x)+1
		while True:
			diff = 0
			next_B = bin(next)[2:]
			for i in range(1,len(next_B)+1):
				if i > len(x_B): 
					diff += 1
					continue
				# print(x_B[-i],"__", next_B[-i])
				if x_B[-i] != next_B[-i]: diff +=1

			if diff <= 2: break
			next += 1
		
		answer.append(next)
	return answer

print(solution([7]))
