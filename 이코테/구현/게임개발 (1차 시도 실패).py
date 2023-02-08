N,M = map(int,input().split()) # N,M은 격자 사이즈 세로/가로
y,x,d = map(int,input().split()) # y,x의 현재 좌표 / d는 바라보는 방향

graph = [list(map(int,input().split())) for _ in range(N)]

dx = [0,1,0,-1]
dy = [1,0,-1,0] # 북 동 남 서
cnt,haha = 1,0

def search(y,x,d):
    global cnt,haha
    for i in range(4):
        ny = y+dy[(d+3)%4] # d=0 -> 3 d=1 ->0  / d=2 -> 1  / d=3 ->2  왼쪽으로 고개돌리는중
        nx = x+dx[(d+3)%4]

    # 조건 1 : 현재 위치에서 현재 방향 기준 왼쪽에 미방문 지역
        if 0<=ny<N and 0<=nx<M:
            if graph[ny][nx] == 0:
                graph[ny][nx] = -1 # 방문했다는 표시
                y = ny
                x = nx # 위치 갱신
        
        # 조건 2 : 현재 위치에서 현재 방향 기준 왼쪽에 방문 지역
        if 0<=ny<N and 0<=nx<M:
            if graph[ny][nx] == -1: # 방문했다면?
                haha+=1 # 고개 돌린 횟수 카운팅
                if haha==4:
                    y=ny-dy[d]
                    x=nx-dx[d] # 고개 돌리지말고 빠꾸함
                    if graph[y][x] == 1: # 바다라면?
                        break
        
    return graph
    
if graph[y][x]==0:
    graph[y][x] = -1
    print(search(y,x,d))
