# 명령어 수는 100가지 제한이므로 초과 우려 X

from collections import deque  # 큐는 모듈을 따로 가져와야함
arr = deque() # 그리고 큐를 선언해준다. 우리가 리스트 선언할 때, arr = [] 하는 것처럼.
T = int(input()) # 실행할 명령횟수
for test_case in range(T): # 명령횟수 루핑
    cmd = list(input().split())  # 명령 입력
    if 'i' in cmd:  # i가 cmd에 있다면
        arr.append(cmd[1]) # i랑 같이 딸려온 데이터 arr에 넣고
    if 'c' in cmd:  # c가 cmd에 있다면?
        print(len(arr)) # 큐 길이(= 원소 몇개있는지 ) 출력
    if 'o' in cmd:  # 큐에서 데이터를 빼는데, 보니까 앞에서 빼네요
        if len(arr)!=0:  # 큐에 원소가 비어있는게 아니라면
            a = arr.popleft() # 큐 앞에 원소 빼세요
            print(a) # 그리고 그거 출력해요
        else:  # 큐에 원소가 없다면
            print("empty")  # 비어있음을 알림
