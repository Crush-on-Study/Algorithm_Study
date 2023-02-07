N,M = map(int,input().split()) # N은 세로 M은 가로
graph = [list(map(int,input().split())) for _ in range(N)] # 그래프 정보 입력받자
arr = [] # 최소값들 받아줄 리스트
min_check = 10001 # 최대 범위가 10000이니까 10001로 하면 무슨 값이 오든 min_check를 상대하는 애가 더 작을 것이다
for col in range(N): # 그래프 행 개수만큼 루핑
    min_check = min(min_check,min(graph[col])) # 각 행의 최소값을 받아주고
    arr.append(min_check) # 그 값을 arr에 넣음
    min_check = 10001  # 다시 min_check 초기화해줘야지

print(max(arr)) # arr에 넣어진 각 행의 최소값들 중에서 제일 큰 애를 출력
