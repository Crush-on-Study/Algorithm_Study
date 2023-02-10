# 왕실의 나이트

graph = [[0]*8 for _ in range(8)]  # 8*8 격자 정보 받기
step = [(2,1),(-2,-1),(1,2),(-1,-2),(2,-1),(-2,1),(1,-2),(-1,2)] # 8방향 스텝

N = input()  # 좌표를 입력받고자 함 (문자열로)
arr = []  # 가로 좌표가 알파벳이라서 리스트 슬라이싱하려고 선언함
cnt = 0 # 이동 가능한 횟수 기록할것임
for idx in range(2): # 좌표는 어차피 x아니면 y니까 2로 했고
    if N[0]: # 가로축인 경우
        arr.append(ord(N[0])-96) # 아스키코드 고려해서 숫자로 변환
    else:
        arr.append(int(N[1])) # 세로축은 정수형으로 단순히 변환만 해주면 되고

def move(y,x):  # 함수 선언해서
    global cnt
    for steps in step: # 8방향스텝 탐색해서
        ny = y+steps[0]
        nx = x+steps[1]
        if 1<=ny<9 and 1<=nx<9: # 경로 벗어나지만 않는다면
            cnt+=1 # 카운팅
    
    return cnt # 결과값 반환

print(move(arr[0],arr[1])) # 결과값 
