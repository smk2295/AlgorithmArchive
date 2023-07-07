# 시간 초과 방지를 위해 sys.stdin.readline() 사용
import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in num:
    print(i)