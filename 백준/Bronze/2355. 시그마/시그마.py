a,b = map(int,input().split())
if a>b:
    a,b=b,a
print(b*(b+1)//2-(a-1)*a//2)