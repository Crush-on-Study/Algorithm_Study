N = int(input())  # 격자 사이즈 받기
graph = [[0]*N for _ in range(N)] # N*N격자

cmd = list(input().split())
direction = ['L','R','U','D'] # L은 왼쪽 한칸 / R은 오른쪽 한칸 / U는 위로 한칸 / D는 아래로 한칸
dx = [-1,1,0,0] # 방향 탐색을 위함
dy = [0,0,-1,1]

def search(y,x): # (1,1) 들어왔다~
    for idx in range(len(cmd)): # cmd R R R U D D 들어왔다치면 6번 돌릴건데
        if cmd[idx] == 'L': # idx=0이 L이면? 근데 R부터 들어왔으니까 이건 아니네 아래로 쭉쭉 가자
            nx = x+dx[0]
            ny = y+dy[0]
            if 0<nx<=N and 0<ny<=N:
                y = ny
                x = nx

        elif cmd[idx] == 'R': # idx=0은 R맞네 그러면
            nx = x+dx[1] # 기존에 0에서 +1
            ny = y+dy[1] # 기존에 0에서 얘는 +0이네
            if 0<nx<=N and 0<ny<=N:  # 이동한 좌표 (0,1)이 맵을 벗어나지 않는 조건 하에 <- (y,x)임 현재
                y = ny # 좌표 갱신해줌
                x = nx 
               # 나머지 절차도 이처럼 똑같이 돌아간다

        elif cmd[idx] == 'U':
            nx = x+dx[2]
            ny = y+dy[2]
            if 0<nx<=N and 0<ny<=N:
                y = ny
                x = nx

        elif cmd[idx] == 'D':
            nx = x+dx[3]
            ny = y+dy[3]
            if 0<nx<=N and 0<ny<=N:
                y = ny
                x = nx
        
    return (y,x)

print(search(1,1)) # 함수에 y=1 / x=1 넣음
