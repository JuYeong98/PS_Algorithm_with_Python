import sys
#공백을 기준으로 구분된 데이터를 입력 받을 때
data = list(map(int, input().split()))

#공백을 기준으로 구분된 데이터가 많지 않다면
a,b,c = map(int, input().split())

#파일 입출력
sys.stdin = open("input.txt", "r")

N,M = map(int, sys.stdin.readline().split())
