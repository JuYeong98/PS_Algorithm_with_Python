N = int(input())
M = int(input())

graph = [[] for _ in range(N)]

for i in range(M):
    a,b = map(int, input().split(' '))
    graph[a-1].append(b)
    graph[b-1].append(a)
#print(graph)    
visited = [0]* (N+1)

def solution(graph, visited, v):
    visited[v] = 1
    #print(v, end=' ')
    for i in graph[v-1]:
        if visited[i] == 0:
            solution(graph, visited, i)

solution(graph, visited, 1)

#print(sum(visited))
#print('hello')
print(sum(visited)-1)