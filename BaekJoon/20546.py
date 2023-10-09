BMP = TIMING = int(input())
chart = list(map(int, input().split()))

num_bmp = 0 #BMP기법으로 거래 시 보유 주식 수 
num_timing = 0 #TIMING기법으로 거래 시 보유 주식 수 
for c in chart:
    r = BMP// c
    BMP = BMP - (r * c)
    num_bmp  +=r 

#print(num_bmp)

up_strike = 0
down_strike = 0
yester_day = 0
today = 0
for i in range(len(chart)):
    if i ==0 :
        yester_day = chart[i]
        today = chart[i]
    else:
        yester_day = today
        today = chart[i]

        if today > yester_day:
            up_strike +=1
            down_strike = 0
        elif today < yester_day:
            down_strike +=1
            up_strike = 0
        elif today == yester_day:
            up_strike = 0
            down_strike = 0
    """        
    print('today = ', end=' ')
    print(chart[i] , end = ' ')
    print('up_strike = ', end=' ')
    print(str(up_strike)+'  down_strike = ' + str(down_strike))        
    """ 
    if up_strike >= 3: #판매하는 경우
        TIMING = TIMING + (num_timing * today)
        num_timing = 0
    if down_strike >=3 :
        r= TIMING // today #구매하는 주식의 개수
        TIMING = TIMING - (r * today)
        num_timing = r   
        #print(num_timing)    

        

TIMING = TIMING + ( num_timing * chart[-1])
BMP = BMP + ( num_bmp * chart[-1])
#print(BMP)
#print(TIMING)

if BMP > TIMING:
    print("BNP")
elif BMP < TIMING:
    print("TIMING")
else:
    print("SAMESAME")    