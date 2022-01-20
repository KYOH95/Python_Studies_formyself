"""
베스트 앨범

link: https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
velog: 

문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.



"""

def solution(genres, plays):

    answer = []
    genres_table = {}
    most_dict = {}
    
    #장르 별로 플레이된 고유번호와 그 고유번호의 플레이 수를 같이 리스트 형태로 저장한다.
    #장르 별로 몇번 플레이가 되었는지 합산 가능한 dictionary "most_dict"를 만든다.
    for i in range(len(genres)):
        try:
            genres_table[genres[i]].append([plays[i],i])
            most_dict[genres[i]] += plays[i]
        except:
            genres_table[genres[i]] = [[plays[i],i]]
            most_dict[genres[i]] = plays[i]

    #가장 많이 재생된 장르의 음악 순으로 정렬한다.
    genres_list = sorted(most_dict, key = lambda x: most_dict[x], reverse = True)

    #장르별로 저장된 고유번호와 그 플레이 횟수를 정렬한다.(플레이횟수가 많은 순서대로, 만약 플레이 횟수가 같다면 고유번호가 낮은 순서대로)
    for key in genres_table:
        genres_table[key].sort(key = lambda x:(-x[0],x[1]))

    #가장 많이 재생된 장르 순서대로 앨범을 작성한다.
    for genre in genres_list:
        temp = genres_table[genre]
        
        # 그장르의 음악이 1개이면 하나만 저장, 2개 이상이면 2개 저장한다.
        if len(temp) == 1:
            answer.append(temp[0][1])
        else:
            answer.append(temp[0][1])
            answer.append(temp[1][1])

    return answer

# print(sorted(dict.items(), key = lambda x: sum(x[1]), reverse = True))