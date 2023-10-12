N = int(input())
M = int(input())
route = [[0 for i in range(N)] for j in range(N)]

start = N*N
phase = 1 # 1은 위로 , 2는 오른쪽, 3은 아래, 4는 왼쪽
route[0][0] = N*N
cnt = N
cnt_copy = N
x= 0
y =0
find = []
for i in range(N*N):
    #print(start)
    #print(x, end=' ')
    #print(y)
    route[x][y] =start
    if start == M:
        find.append(x+1)
        find.append(y+1)
    if phase ==1:
        cnt -=1
        if cnt == 0:
            cnt_copy -=1
            cnt = cnt_copy
            phase = 2
            y +=1
            #route[x][y] = start
            start-=1
        else:
            #route[x][y] = start    
            x+=1
            start -=1
    elif phase ==2:
        cnt -=1
        if cnt ==0:
            cnt = cnt_copy
            phase = 3
            x-=1
            #route[x][y] = start
            start -=1
        else:    
            #route[x][y] = start    
            y+=1
            start-=1    
    elif phase ==3:
        cnt-=1
        if cnt ==0:
            cnt_copy -=1
            cnt = cnt_copy
            phase = 4
            y-=1
            #route[x][y] = start
            start-=1
        else:    
            #route[x][y] = start    
            x-=1
            start-=1    
    elif phase ==4:
        cnt-=1
        if cnt == 0:
            cnt = cnt_copy
            phase = 1
            x+=1
            #route[x][y] = start
            start-=1
        else:
            #route[x][y] = start    
            y-=1
            start -=1
for i in range(N):
    print(' '.join(str(s) for s in route[i]))           
print(' '.join(str(s) for s in find))