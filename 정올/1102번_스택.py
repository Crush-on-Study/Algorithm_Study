# 해당 문제 해석
# 명령의 수는 최대 100까지 가능. 초과 우려 X (배열에 끊임없이 데이터를 넣을 수 있는건 10만아래)

arr = [] # 스택을 담아줄 배열
T = int(input()) # 명령 실행횟수
for test_case in range(T): # T만큼 돌려서
    cmd = list(input().split()) # 명령어를 입력하고 split을 통해 공백기준 리스트화 시킴
    if 'i' in cmd: # 명령어에 i가 들어가 있다면
        arr.append(cmd[1]) # i랑 함께 들어온 데이터'만' 추가함. (EX. i 7의 경우는 ['i','7'] 로 들어오니까 cmd[1] = 7)
    if 'c' in cmd: # c는 스택에 존재하는 데이터 수를 말하라는 것. 그럼? 배열 길이와 같지
        print(len(arr))
    if 'o' in cmd: # 스택에서 데이터를 빼고 데이터를 출력하라는 것
        if len(arr)!=0: # 스택이 현재 비어있지않다면
            a = arr.pop()
            print(a) # 원소 꺼내서 보여주고
        else: # 스택이 비어있다면
            print("empty") # 비어있음을 알림
