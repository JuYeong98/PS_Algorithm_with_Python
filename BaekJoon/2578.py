board = []
for i in range(5):
    num = list(map(int, input().split()))
    board.append(num)

bingo =[]
for i in range(12):
    if i < 5:
        bingo.append(board[i])
    elif i >=5 and i< 10:
        bingo.append([board[j][i-5] for j in range(5)])
    elif i == 10:
        bingo.append([board[j][j] for j in range(5)])        
    elif i == 11:
        bingo.append([board[4-j][j] for j in range(5)]) 


teacher =[]
for i in range(5):
    num = list(map(int, input().split()))
    for n in num:
        teacher.append(n)
#print(teacher)
answer =0
#print('------------------')
for i in range(len(teacher)):
    for b in bingo:
        if teacher[i] in b:
            b.remove(teacher[i])
    answer = 0 
    for b in bingo:
        if len(b) == 0:    
            answer +=1
    if answer>=3:
        print(i+1)
        break
    #print(bingo)               
#print()         
#print(bingo)        
#print(teacher)