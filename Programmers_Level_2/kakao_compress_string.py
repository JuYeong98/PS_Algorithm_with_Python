def solution(s):
    answer = 0
    solution = ""
    len_s = len(s)
    l = []
    small = []
    for i in range(1,len_s+1):
        if len_s % i ==0:
            small.append(i)
    min_length = 1001
    for i in range(1, len_s+1):
        sub_list = []
        for j in range(0,len_s, i):
            sub_list.append(s[j : j+i])
        strikes =1
        sub_list.append('')
        #print(sub_list)
        for i in range(len(sub_list)-1):
            if sub_list[i] == sub_list[i+1]:
                strikes +=1
            else:
                if strikes == 1:
                    solution+=sub_list[i]
                else:
                    solution = solution + str(strikes)+ sub_list[i]
                    #print(str(strikes)+ sub_list[i])
                strikes =1    
        #print(solution)
        if len(solution) < min_length:
            min_length = len(solution)
        solution = ''
    return min_length