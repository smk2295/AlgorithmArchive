N = int(input())
for i in range(N):
    i += 1
    print("*"*(i)+" "*(2*N-(2*i))+"*"*(i))
for i in range(N-1):
    i += 1
    print("*"*(N-i)+" "*(2*i)+"*"*(N-i))