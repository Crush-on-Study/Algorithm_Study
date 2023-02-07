N,K = map(int,input().split()) # N은 숫자 K는 N이랑 나눌 애
cnt = 0
while N>1:
    if N%K==0: # 나눠떨어지면
        N = N//K
        cnt+=1
    else:
        N-=1
        cnt+=1
print(cnt)

# 풀기 전에 그리디 적용이 가능한지 꼭 확인하기.
