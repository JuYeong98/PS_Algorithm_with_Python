from itertools import combinations
from collections import deque
N, M = map(int,input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

virus = deque() # 바이러스 좌표 덱
block = deque() # 벽 좌표 덱 
point = [] # 벽을 놓을 수 있는 좌표 스택

# 벽 3개 좌표 조합 생성
# 바이러스 위치 확인
# 벽 위치 확인
for i in range(N) :
  for j in range(M) :
    if matrix[i][j] == 2 :
      virus.append([i,j])
    elif matrix[i][j] == 1 :
      block.append([i,j])
    else :
      point.append([i,j])

answer = 0
di = [1,-1,0,0]
dj = [0,0,1,-1]
for p in combinations(point, 3) :
  one, two, thr = p # 벽 3개

  # 각 점을 벽으로 만들기
  matrix[one[0]][one[1]] = 1
  matrix[two[0]][two[1]] = 1
  matrix[thr[0]][thr[1]] = 1

  visit = [[False]*M for _ in range(N)]
  for v in virus :
    visit[v[0]][v[1]] = True

  # 바이러스 전파시키기
  queue = virus.copy()
  while queue :
    i,j = queue.popleft()

    for d in range(4) :
      ni = i + di[d]
      nj = j + dj[d]

      if ni < 0 or ni >= N or nj < 0 or nj >= M : continue

      if matrix[ni][nj] == 0 and visit[ni][nj] == False:
        visit[ni][nj] = True
        queue.append([ni,nj])

  safeArea = 0
  for i in range(N) :
    for j in range(M) :
      if matrix[i][j] == 0 and visit[i][j] == False :
        # 벽이 놓여있지 않고, 방문하지 않았다면
        # 바이러스가 퍼지지 않은 것
        safeArea += 1

  answer = max(answer, safeArea)
  
  # 벽으로 만든 부분 다시 돌려놓기
  matrix[one[0]][one[1]] = 0
  matrix[two[0]][two[1]] = 0
  matrix[thr[0]][thr[1]] = 0

print(answer)