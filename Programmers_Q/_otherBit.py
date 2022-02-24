"""
2개 이하로 다른 비트
link: https://programmers.co.kr/learn/courses/30/lessons/77885?language=python3
"""
	
def solution(numbers):
	answer = []
	
	for x in numbers:
		x_bin = str(bin(x))[2:]
		num = x+1
		count = 3
		while count > 2:
			num_bin = str(bin(num))[2:]
			i = 1
			count = 0
			while i <= len(num_bin):
				if i > len(x_bin):
					if num_bin[-i] == '1': count += 1
				elif num_bin[-i] != x_bin[-i]: count +=1
				i+=1
			num+=1
			# print(x_bin,num_bin,count)
		
		answer.append(int(num_bin,2))
	return answer

print(solution([2,7]))
