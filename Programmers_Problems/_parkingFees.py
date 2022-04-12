"""
주차 요금 계산
link: https://programmers.co.kr/learn/courses/30/lessons/92341
velog: 


"""

def solution(fees, records):
    answer = []
    parkingLot = {}
    total_fees = {}

    for x in records:
        time = x.split(" ")[0]
        hour_, min_ = time.split(":")[0],time.split(":")[1]
        number = x.split(" ")[1]
        act = x.split(" ")[2]

        #차가 주차장으로 들어올때
        if act == "IN":
            parkingLot[number] = int(hour_)*60 + int(min_)
            if number not in total_fees:
                total_fees[number] = 0
        
        #차가 주차장에서 나갈때
        else:
            total_fees[number] += int(hour_)*60 + int(min_) - parkingLot[number]
            del parkingLot[number]

    #주차장에 남아있는 차들 23:59 기준으로 정산
    for car in parkingLot:
        total_fees[car] += 23*60+59 - parkingLot[car]

    #금액 계산 후 정답 리스트에 저장
    for keys in sorted(total_fees):
        
        #5000 + ⌈(334 - 180) / 10⌉ x 600 = 14600
        day_fee = fees[1]
        if (total_fees[keys] - fees[0]) % fees[2] == 0:
            day_fee += ((total_fees[keys] - fees[0])//fees[2]) *  fees[3]
        else: 
            day_fee += (((total_fees[keys] - fees[0])//fees[2])+1) *  fees[3]
        
        #기본요금이 안넘을 경우 > 기본요금을 채우기
        if day_fee <= fees[1]:
            day_fee = fees[1]

        answer.append(day_fee)
        
    return answer


# solution([180, 5000, 10, 600],["05:34 5961 IN", "06:54 5961 OUT"])
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))