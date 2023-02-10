N,K = map(int,input().split()) # N은 숫자 개수 / K는 몇개 뽑니
number = list(map(int,input().split())) # K개만큼 숫자 뽑고
arr,result = [],[] # 리스트 2개 지정해놓고
def backtrack(num,start): # 
    if num==K:
        result.append(list(arr))
    for i in range(start,N+1):
        arr.append(i)
        backtrack(num+1,i+1)
        arr.pop()
    
    return result

a = (backtrack(0,1)) # 백트래킹 호출해서

for next in range(len(a)):
    if number==a[next]:
        try: # 앙 트라이 익셉트 
            print(*a[next+1])
        except: IndexError : print("NONE")
