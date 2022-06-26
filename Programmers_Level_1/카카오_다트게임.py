
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

    def solution(dartResult):
    answer = 0
    number =[0]
    option = []
    for i in range(len(dartResult)):
        if ord(dartResult[i]) <=57 and ord(dartResult[i])>=48:
            if i>=1: 
                if ord(dartResult[i-1]) <=57 and ord(dartResult[i-1])>=48:
                    continue
            if ord(dartResult[i+1]) <=57 and ord(dartResult[i+1])>=48:
                number.append(10)
            else:    
                number.append(int(dartResult[i]))
        else:
            option.append(dartResult[i])
    print(number)        
    print(option)
    count = 0
    for i in range(1, len(number)):
        for j in range(count , len(option)):
            if option[j] =='#':
                number[i] = -number[i]
                count +=1
                break
            elif option[j] =='*':
                number[i] = 2* number[i]
                number[i-1] = 2 * number[i-1]
                count +=1
                break
            if option[j] =='D':
                number[i] = pow(number[i] , 2)
                count +=1
            elif option[j] =='T':
                print('check')
                number[i] = pow(number[i],3)
                count +=1
            elif option[j] =='S':
                count +=1
            if j < len(option)-1:
                if option[j+1] =='*' or option[j+1] =='#':
                    continue
                else:
                    break
                
    for num in number:
        answer+=num
                
    print(number)
    return answer
solution('10D10S#10S')