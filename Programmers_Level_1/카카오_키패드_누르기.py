def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer

def solution(numbers, hand):
    answer = ''
    def cal_distance(cur , to_push):
        if to_push == 0:
            if cur ==-1  or cur ==8 :
                return 1
            elif cur ==7 or cur==9 or cur ==5:
                return 2
            elif cur ==4 or cur ==6 or cur ==2:
                return 3
            elif cur ==1 or cur ==3:
                return 4
            elif cur==0:
                return 0
        elif to_push ==2:
            if cur ==2:
                return 0
            elif cur ==1 or cur==3 or cur==5:
                return 1
            elif cur ==4 or cur==6 or cur ==8:
                return 2
            elif cur ==7 or cur ==9 or cur ==0:
                return 3
            elif cur ==-1:
                return 4
        elif to_push ==5:
            if cur ==5:
                return 0
            elif cur ==2 or cur ==4 or cur==6 or cur ==8:
                return 1
            elif cur ==1 or cur ==3 or cur ==7 or cur ==9 or cur ==0:
                return 2
            elif cur ==-1:
                return 3
        elif to_push ==8:
            if cur ==8:
                return 0
            elif cur ==5 or cur ==7 or cur ==0 or cur ==9:
                return 1
            elif cur ==2 or cur ==-1 or cur == 4 or cur ==6 :
                return 2
            elif cur ==1 or cur ==3:
                return 3
    cur_left = -1
    cur_right = -1
    for number in numbers:
        if number ==1 or number == 4 or number ==7 :
            answer+='L'
            cur_left = number
        elif number == 3 or number ==6 or number ==9:
            answer+='R'
            cur_right = number
        else:
            dis_left, dis_right =  cal_distance(cur_left, number) ,cal_distance(cur_right, number)
            #print('number: ',number, end='  ')
            #print('왼손 거리: ', dis_left, end=' ')
            #print('오른손 거리: ' ,dis_right)
            if dis_left <dis_right:
                cur_left = number
                answer+='L'
            elif dis_left > dis_right:
                cur_right = number
                answer+='R'
            elif dis_right ==dis_left:
                if hand=='right':
                    cur_right = number
                    answer+='R'
                else:
                    cur_left = number
                    answer+='L'
    return answer    