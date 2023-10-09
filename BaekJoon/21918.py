def reverse_num(num):
    if num == 0:
        return 1
    elif num ==1:
        return 0    

N, M = map(int, input().split()) #N은 전구의 개수, M은 명령어의 개수 
light = list(map(int , input().split()))
for i in range(M):
    action = list(map(int, input().split()))
    
    if action[0] == 1:
        light[action[1]-1] = action[2]
    elif action[0] == 2:
        for i in range(action[1]-1, action[2]):
            light[i] = reverse_num(light[i])
    elif action[0] == 3:
        for i in range(action[1]-1, action[2]):
            light[i] = 0
    elif action[0] == 4:
        for i in range(action[1]-1, action[2]):
            light[i] = 1


for i in range(len(light)):
    print(light[i],end = ' ')
