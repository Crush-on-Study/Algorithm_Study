# 함수를 나누자

N,M = map(int,input().split()) # N은 세로 M은 가로
y,x,d = map(int,input().split()) # y좌표 x좌표 d는 바라보는 방향
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)] # 방문 경로 기록

cnt = 1
gogae = 0

dx = [0,-1,0,1]
dy = [-1,0,1,0] # 북 서 남 동 


def search(y,x):
    global cnt,gogae
    visited[col][row] = True # 방문해앳!
    for i in range(4):
        ny = y+dy[i%4]
        nx = x+dx[i%4] # d=0 북쪽 / d+3)%4 해버리면? 서쪽. 고개돌렸어어
        # ny = y+dy[(d+3)%4]  <- 이게 원인이였다. 
        if 0<=ny<N and 0<=nx<M:
            if not visited[ny][nx] and graph[ny][nx] == 0: # 미방문했고 육지라면
                visited[ny][nx] = True
                cnt+=1
                gogae = 0
                search(ny,nx)
                
            else:
                gogae+=1
                if gogae == 4:
                    ny = y-dy[(d+3)%4]
                    nx = x-dx[(d+3)%4]
                    if visited[ny][nx] == True or graph[ny][nx] == 1: # 바다라면
                        break
                    else:
                        gogae = 0 # 고개 돌린 카운팅 리셋하고                            
                        y = ny
                        x = nx
                        search(y,x)
                        
    return cnt
    

for col in range(N):
    for row in range(M):
        if not visited[col][row] and graph[col][row] == 0: # 미방문했고 육지인 곳
            a = search(col,row) # search 호출
            
print(a)
