list = []
for i in range(1,6):
    name =input()
    if "FBI" in name:
        list.append(i)

if list:
    print(*list)
else:
    print("HE GOT AWAY!")