
def solution(genres, plays):
    
    dict = {id:[] for id in genres}
    
    for i in range(len(genres)):
        dict[genres[i]].append(plays[i])

    print(sorted(dict.items(), key = lambda x: sum(x[1]), reverse = True))
    
    print(dict)
        
    
        
    
    answer = []
    return answer


solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500])