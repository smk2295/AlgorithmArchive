N = int(input())
for i in range(N-1):
    i += 1
    print(" "*(N-i)+"*"*i)
for i in range(N):
    i += 1
    print(" "*(i-1)+"*"*(N+1-i))