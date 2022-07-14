import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)


def solution(str1, str2):
    answer = 0
    str1 = str1.upper()
    str2 = str2.upper()
    str1_list = []
    str2_list = []
    for i in range(len(str1)-1):
        if ord(str1[i]) <=90 and ord(str1[i]) >=65 and ord(str1[i+1]) <=90 and ord(str1[i+1]) >=65:
            str1_list.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if ord(str2[i]) <=90 and ord(str2[i]) >=65 and ord(str2[i+1]) <=90 and ord(str2[i+1]) >=65:
            str2_list.append(str2[i:i+2])
    if len(str1_list) ==0 and len(str2_list) ==0 :
        return 65536
    str1_list_temp = str1_list.copy()
    str1_list_answer =str1_list.copy()
    for i in str2_list:
        if i not in str1_list_temp:
            str1_list_answer.append(i)
        else:
            str1_list_temp.remove(i)
    result = []     
    for i in str2_list:
        if i in str1_list:
            str1_list.remove(i)
            result.append(i)
    #print(str1_list_answer)
    #print(result)
    return   65536 * len(result) //len(str1_list_answer)    