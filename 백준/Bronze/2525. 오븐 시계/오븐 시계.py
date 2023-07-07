A, B = map(int,input().split())
C = int(input())

if (B+C)>=60:
    hr=(B+C)//60
    min=(B+C)%60
    if (A+hr)>=24:
        print(A+hr-24,min)
    else:
        print(A+hr,min)
else: print(A,B+C)