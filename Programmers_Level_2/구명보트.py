def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    #print(people)
    boat = []
    remain = []
    for person in people:
        if person > limit//2:
            boat.append(person)
        else:
            remain.append(person)
    #print(boat)       
    count =0
    remain.sort()
    for i in range(len(boat)): #무거운 애들 무거운 순서대로 가벼운 친구들과 매칭
        if remain:
            if boat[i] + remain[0] > limit: #i번째 놈과 남아있는 사람 중 가장 가벼운 사람과 합했을 때 기준을 넘는다면
                continue #PASS
            else:#둘이서 탈 수 있다면
                boat[i] +=remain[0] #더해주고
                del remain[0] #남아있는 사람 제거
        else:
            break
    print(boat)       
    print(remain)
    return len(boat) + ((len(remain)+1)//2)