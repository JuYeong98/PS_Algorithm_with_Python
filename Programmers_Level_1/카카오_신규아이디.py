def solution(new_id):
    answer = []
    new_id = list(new_id)
    strikes= 0
    for i in range(len(new_id)):
        ch = new_id[i]
        ord_num = ord(new_id[i])
        if ord_num >=97 and ord_num <=122:
            answer.append(ch)
            strikes =0 
        elif ord_num >=65 and ord_num <=90:
            answer.append(new_id[i].lower()) 
            strikes =0
        elif (ord_num <=57 and ord_num>=48) or ch=='-' or ch =='_' or ch=='.':
            if ch =='.':
                strikes+=1
            else:
                strikes = 0
            if strikes >1:
                continue
            answer.append(new_id[i])
    answer = ''.join(s for s in answer)  
    if answer[0] =='.':
        answer = answer[1:]  
    if len(answer)>1:
        if answer.strip()[-1] == '.':
            answer = answer[:-1]
    l = len(answer)
    if l ==0 :
        return 'aaa'
    elif l ==1:
        return answer + answer + answer
    elif l ==2:
        return answer+ answer[-1:]
    
    if l >15:
        answer = answer[:15]
    if answer.strip()[-1] == '.':
        answer = answer[:-1]
        
    
    print(str(answer))    
    return answer

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer        