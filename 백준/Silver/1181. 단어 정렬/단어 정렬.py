n = int(input())

word = [str(input()) for i in range(n)]

#set을 이용해 중복 제거
word = list(set(word))

#사전 순 정렬 후, 길이 순 정렬
word.sort()
word.sort(key=len)

for i in word:
    print(i)