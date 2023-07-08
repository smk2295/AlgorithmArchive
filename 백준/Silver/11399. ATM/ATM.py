N = int(input())
cnt = 0
total = 0

P = list(map(int, input().split()))
P.sort()

for j in range(N):
    cnt+=P[j]
    total+=cnt
print(total)