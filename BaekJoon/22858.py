N,K=map(int,input().split())

result=list(map(int,input().split()))
pattern=list(map(int,input().split()))

start=result

for i in range(K):
    #N의 크기에 맞는 임시리스트 선언
    tmp=list(range(N))
    for j in range(N):
        #패턴대로 앞부터 자리를 가준다.
        go=pattern[j]
        tmp[go-1]=start[j]
    start=tmp

print(start,end=' ')