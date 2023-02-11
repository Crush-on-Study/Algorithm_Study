import sys
sys.stdin = open("111.txt")
from collections import deque

N,M = map(int,input().split()) # N은 세로  M은 가로
graph = [list(map(int,input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

result = 0

# DFS이풀이
def dfs_solution():
    def dfs(y,x):
        global result
            
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    if ny == N-1 and nx==M-1:
                        graph[ny][nx] = graph[y][x]+1
                        result = graph[ny][nx]
                        break
                    else:
                        graph[ny][nx] = graph[y][x]+1
                        visited[ny][nx] = True
                        dfs(ny,nx)
                        
        return result


    for col in range(N):
        for row in range(M):
            if graph[col][row] == 1 and not visited[col][row]:
                visited[col][row] = True
                a = dfs(col,row)
                
    print(a)
    
dfs_solution()

# BFS 풀이
def bfs_solution():
    def bfs(y,x):
        global result
        q = deque()
        q.append((y,x))
        
        while q:        
            y,x = q.popleft()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]            
                if 0<=ny<N and 0<=nx<M:
                    if not visited[ny][nx] and graph[ny][nx] == 1:
                        if ny==N-1 and nx==M-1:
                            graph[ny][nx] = graph[y][x]+1
                            result = graph[ny][nx]
                            
                        else:
                            visited[ny][nx] = True
                            graph[ny][nx] = graph[y][x]+1
                            q.append((ny,nx))
                            
        return result
                        
        

    for col in range(N):
        for row in range(M):
            if graph[col][row] == 1 and not visited[col][row]:
                visited[col][row] = True
                a = bfs(col,row)
                
    print(a)

bfs_solution()
