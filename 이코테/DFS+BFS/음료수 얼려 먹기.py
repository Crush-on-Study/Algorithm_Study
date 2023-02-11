import sys
sys.stdin = open("111.txt")
from collections import deque
N,M = map(int,input().split()) # N은 세로 M은 가로
graph = [list(map(int,input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

cnt = 0


# DFS 
def dfs_solution():
    def dfs(y,x):
        global cnt
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0>ny or ny>=N or 0>nx or nx>=M:
                continue

            if graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                cnt+=1
                dfs(ny,nx)

        return cnt

    arr = []

    for col in range(N):
        for row in range(M):
            if graph[col][row] == 0 and not visited[col][row]:
                visited[col][row] = True
                cnt = 1
                a = dfs(col,row)
                arr.append(a)

    print(len(arr))
    
dfs_solution()

# BFS 풀이
def bfs_solution():
    def bfs(y,x):
        global cnt
        q = deque()
        q.append((y,x))
        
        while q:
            y,x= q.popleft()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<N and 0<=nx<M:
                    if graph[ny][nx] == 0 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        cnt+=1
                        q.append((ny,nx))
                        
        return cnt

    arr = []

    for col in range(N):
        for row in range(M):
            if graph[col][row] == 0 and not visited[col][row]:    
                visited[col][row] = True
                cnt = 1
                a = bfs(col,row)
                arr.append(a)
                
    print(len(arr))

bfs_solution()
