def solution(x):
    n=x
    sum=0    
    while n>0:
        sum+=n%10
        n=n//10
    
    if x%sum==0:
        return True
    else:
        return False
