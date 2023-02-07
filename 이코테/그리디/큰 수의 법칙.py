# 간단한 그리디인데도 사소한거 놓쳐서 시간 걸렸던 문제
# 고민 충분히하고 짜자. 바로 짜면 오히려 오래 걸린다

N,M,K = map(int,input().split())  # 숫자 개수 / 몇번 더할 것인지 / 같은 수는 최대 몇번만 가능한지?
Chance = K # k가 소진될 때마다 충전해줄 변수
arr = list(map(int,input().split()))  # 숫자 입력받고
arr.sort(reverse=True) # 역순 쏘트
tot = 0  # 결과값 담을 변수
for i in range(1,M+1): # M번 더할꺼니까 루핑
    if K!=0: # 아직 초과된게 아니라면
        tot+=arr[0] # 계속해서 제일 큰값 더해주고
        K-=1 # 차감
    elif K==0: # k==0되면
        tot+=arr[1] # 두번째로 큰값 더해주고
        K = Chance # k 채워줘
print(tot)
