N,M = map(int,input().split()) # N,M은 격자 사이즈 세로/가로
y,x,d = map(int,input().split()) # y,x의 현재 좌표 / d는 바라보는 방향

graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [0,-1,0,1]
dy = [1,0,-1,0] # 북 서 남 동  // 왼쪽으로 고개 돌리는 거임

cnt,gogae = 1,0

def search(y,x):
    global cnt,gogae
    for i in range(4):
        ny = y+dy[(d+1)%4]
        nx = x+dx[(d+1)%4] # 고개 돌리는거임 왼쪽으로
        if 0<=ny<N and 0<=nx<M:
            if not visited[ny][nx] and graph[ny][nx]==0:
                visited[ny][nx] = True # 방문해요옷
                cnt+=1
                gogae+=1
                y = ny
                x = nx # 좌표 갱신
            elif visited[ny][nx] == True or graph[ny][nx]==1:
                gogae+=1
                if gogae==4: # 4방향 다 돌았는디 ㅠ
                    ny = y-dy[d]
                    nx = x-dx[d] # 방향 유지한 채로 뒤로가쟈
                    if graph[ny][nx] == 1: # 바다인 경우
                        break
    
    return cnt
        

for col in range(N):
    for row in range(M):
        if graph[col][row] == 0 and not visited[col][row]:
            graph[col][row] == -1
            visited[col][row] = True
            a = search(col,row)

print(a)
