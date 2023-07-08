T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack: # 스택이 채워져 있다면
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack: # 스택이 비어 있다면
            print("YES")
        else:
            print("NO")