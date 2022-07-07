def solution(record):
    answer = []
    id_dict ={}
    for r in record:
        ID = r.split(' ')[1]
        name = r.split(' ')[-1]
        in_out = r.split(' ')[0]
        if in_out != 'Leave':
            id_dict[ID] = name
    #print(id_dict)    
    for r in record:
        ID = r.split(' ')[1]
        in_out = r.split(' ')[0]
        ment = ''
        name = id_dict[ID]
        if in_out == 'Enter':
            ment = name+'님이 들어왔습니다.'
            answer.append(ment)
        elif in_out=='Leave':
            ment = name+'님이 나갔습니다.'
            answer.append(ment)    
    return answer