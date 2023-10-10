def switch(n):
    if n == 0:
        return 1
    else:
        return 0
N = int(input())
light = list(map(int, input().split()))
M = int(input())

for m in range(M):
    gender, pos =map(int, input().split())
    if gender == 1:
        val = N // pos
        for i in range(1, val+1):
            #print(light[(pos*i)-1])
            light[(pos*i)-1] = switch(light[(pos*i)-1])
    else:
        if pos == N:
            light[pos-1] = switch(light[pos-1])
        elif pos ==1:
            light[0] = switch(light[0])
        else:
            list_1 = light[:pos]
            list_1 = list_1[::-1]
            list_2 = light[pos+1:]
            len_list_1 = len(list_1)
            len_list_2 = len(list_2)
            short_one = len_list_1 if len_list_1 <= len_list_2 else len_list_2
            cnt = 0
            for i in range(short_one):
                if list_1[i] == list_2[i]:
                    cnt+=1
            for i in range(pos-cnt-1, pos+cnt):
                light[i] = switch(light[i])
       

for i in range(N):
    print(light[i], end = " ")
    if (i+1) % 20 == 0 :
        print()    
