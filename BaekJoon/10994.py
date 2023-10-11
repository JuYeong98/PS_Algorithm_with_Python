N = int(input())
def star_map(star, width, plus):
    #print(width)
    #print(plus)
    for i in range(width):
        if i == 0 or i == width-1: #처음이거나 마지막이거나
            for j in range(width):
                star[i+plus][j+plus] = '*'
        else:
            for j in range(width):
                if j == 0 or j ==width-1:
                    star[i+plus][j+plus] ='*'
                else:
                    star[i+plus][j+plus] = ' '            
    return star                
if N ==1:
    print('*')


else:
    width = 4*(N-1) + 1 
    height = width
    
    star = [['' for j in range(width)] for i in range(width)] 
    for i in range(N):
        star = star_map(star, width - (4*i), i*2)
        
for i in range(width):
    s = ''.join(star[i])    
    print(s)   