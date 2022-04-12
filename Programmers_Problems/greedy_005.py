"""
단속 카메라
link: https://programmers.co.kr/learn/courses/30/lessons/42884?language=python3
"""

def solution(routes):
	routes.sort(key = lambda x:(x[1],-x[0]))
	camera = []
	for x in routes:
		camera_check = False
		for y in camera:
			if y >= x[0] and y<=x[1]: 
				camera_check = True
				break
		if camera_check == False:
			camera.append(x[1])

	return len(camera)

solution([[-20,-15],[-14,-5],[-18,-13],[-5,-3]])
# solution([[-20,-15],[-14,-15],[-18,-15],[-5,-15]])
