def solution(price, money, count):
    
    s =0
    for i in range(1,count+1):
        s+=i
    s*=price
    
    return abs(money-s) if money < s else 0