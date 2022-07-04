def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer

def solution(board, moves):
    answer = 0
    result =[]
    sub = []
    arr_2d = []
    for i in range(len(board)):
        arr_2d.append([])
    for i in range(len(board)):    
        for j in range(len(board[0])):
            if board[i][j] !=0:
                arr_2d[j].append(board[i][j])
                #arr_2d[j][i] = board[i][j]        
    for i in range(len(moves)):
        sub_list = arr_2d[moves[i]-1]
        print('move: ',moves[i] , end=' ')
        print(sub_list)
        if sub_list !=[]:
            result.append(sub_list[0])
            sub.append(sub_list[0])
            del arr_2d[moves[i]-1][0]
            if len(result) >=2 and (result[-1] == result[-2]):
                del result[-1]
                del result[-1]   
    return len(sub) - len(result)