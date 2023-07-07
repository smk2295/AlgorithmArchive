a,b = map(int,input().split())
if a>b:
    a,b=b,a
#가우시안 공식 사용 : 1~n 까지의 합 = n*(n+1)/2
print(b*(b+1)//2-(a-1)*a//2)
