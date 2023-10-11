left, right = input().split()

def cal_distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
keyboard_left = {'q' :[0,1 ], 'w' : [1,1], 'e' : [2,1], 'r' : [3,1], 't' : [4,1] , 'a':[0,0], 's' : [1,0], 'd' :[2,0],'f':[3,0],'g':[4,0],'z':[0,-1],'x':[1,-1],'c':[2,-1],'v':[3,-1]}
keyboard_right = {'y':[5,1],'u':[6,1],'i':[7,1],'o':[8,1],'p':[9,1],'h':[5,0],'j':[6,0],'k':[7,0],'l':[8,0],'b':[4,-1],'n':[5,-1],'m':[6,-1]}

sentence = list(input())
#print(sentence)
dis = 0
for s in sentence:
    if s in keyboard_left:
        dis +=cal_distance(keyboard_left[left] , keyboard_left[s]) +1
        #print(dis)
        left = s
    else:
        dis+= cal_distance(keyboard_right[right], keyboard_right[s]) +1
        #print(dis)
        right = s
#print(keyboard_left)
#print(keyboard_right)
print(dis)