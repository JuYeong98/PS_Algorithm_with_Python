def solution(s):
    answer = []
    s = s[1:-1]
    answer_set =set()
    s= list(s)
    sub_str=''
    for i in range(len(s)):
        #print(s[i])
        if s[i] ==',':
            if s[i-1] !='}':
                sub_str+=s[i]
            else:
                sub_str+=' '
        else:
            sub_str+=s[i]
    #print(sub_str)   
    sub_str_list = sub_str.split(' ')
    #print(sub_str_list)
    sub_list = []
    for sub in sub_str_list:
        sub_list.append(sub[1:-1])
    sub_list.sort(key = len)
    for sub in sub_list:
        s = sub.split(',')
        for small in s:
            #print(small)
            if int(small) not in answer:
                answer.append(int(small))

    return answer


def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer