def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
def solution(id_list, report, k):
    answer = []
    reported_dict={}
    report_dict={}
    report = list(set(report))

    for id in id_list:
        reported_dict[id] =0
        report_dict[id] = []
        #answer.append(0)

    for r in report:
        reporter = r.split(' ')[0]
        reported = r.split(' ')[-1]
        #print('신고자 : ', reporter , '신고받음 : ' ,reported)
        reported_dict[reported]+=1
        report_dict[reporter].append(reported)
    #print(reported_dict)    
    #print(report_dict)
    count = 0

    for key in report_dict:
        sub_list = report_dict[key]
        for sub in sub_list:
            if reported_dict[sub] >=k:
                count+=1
        answer.append(count)
        count =0
    return answer    