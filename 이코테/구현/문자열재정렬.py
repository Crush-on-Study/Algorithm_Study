# 322페이지 / 구현 - 문자열 재정렬 문제
# 문자열 길이 1만이 최대라서 완탐해도 노상관

from collections import deque # 데큐 가져와서
s = input()  # 문자열 입력받고
num = [str(k) for k in range(10)] # 0부터 9까지 담아놓고 문자열 s에서 숫자(문자열타입이긴하지만)가 있는지 확인하고자 함
arr = deque() # 데큐 선언
arr2= [] # 결과값 담을 리스트 선언
tot = 0 # 숫자들 합 저장할 변수 초기화
for i in s: # 문자열 s 탐색해가면서
    arr.append(i) # 데큐에 한글자 한글자씩 박아둠

while arr: # 데큐가 비어있지 않다면
    if arr[0] in num:  # 가장 앞에 있는애가 0~9에 해당하는 숫자(문자열타입이긴하지만)인가?
        z = arr.popleft() # 그렇다면 popleft해서
        tot+=int(z)  # 정수변환한다음에 tot에 계속 합계 갱신하자
        
    else: # 숫자가 아니라면
        k = arr.popleft() # 꺼내서
        arr2.append(k) # 결과값 담을 리스트에 담아놓자

arr2.sort() # 오름차순 정렬하고
arr2.append(tot) # 마지막에 숫자들 합 구한거 박아둔 뒤
print(''.join(map(str,arr2))) # 결과 
